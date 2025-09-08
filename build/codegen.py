from llvmlite import ir, binding
from build.my_ast import Number, BinOp, Assign, Var, FunctionDef, FunctionCall, Return, Print, Input, StringLiteral, ArrayLiteral, ArrayAccess

class CodeGen:
    def __init__(self):
        binding.initialize()
        binding.initialize_native_target()
        binding.initialize_native_asmprinter()

        self.module = ir.Module(name="main")
        self.module.triple = binding.get_default_triple()

        voidptr_ty = ir.IntType(8).as_pointer()
        printf_ty = ir.FunctionType(ir.IntType(32), [voidptr_ty], var_arg=True)
        self.printf = ir.Function(self.module, printf_ty, name="printf")

        scanf_ty = ir.FunctionType(ir.IntType(32), [voidptr_ty], var_arg=True)
        self.scanf = ir.Function(self.module, scanf_ty, name="scanf")

        func_type = ir.FunctionType(ir.IntType(32), [])
        self.main_func = ir.Function(self.module, func_type, name="main")

        block = self.main_func.append_basic_block(name="entry")
        self.builder = ir.IRBuilder(block)

        self.variables = {}
        self.functions = {}

        fmt_int = "%d\n\0"
        self.fmt_str_int = ir.GlobalVariable(self.module, ir.ArrayType(ir.IntType(8), len(fmt_int)), name="fmtstrint")
        self.fmt_str_int.linkage = 'internal'
        self.fmt_str_int.global_constant = True
        self.fmt_str_int.initializer = ir.Constant(ir.ArrayType(ir.IntType(8), len(fmt_int)),
                                                   bytearray(fmt_int.encode("utf8")))

        fmt_scan = "%d\0"
        self.fmt_str_scan = ir.GlobalVariable(self.module, ir.ArrayType(ir.IntType(8), len(fmt_scan)), name="fmtstrscan")
        self.fmt_str_scan.linkage = 'internal'
        self.fmt_str_scan.global_constant = True
        self.fmt_str_scan.initializer = ir.Constant(ir.ArrayType(ir.IntType(8), len(fmt_scan)),
                                                    bytearray(fmt_scan.encode("utf8")))

    def print_int(self, val):
        fmt_ptr = self.builder.bitcast(self.fmt_str_int, ir.IntType(8).as_pointer())
        self.builder.call(self.printf, [fmt_ptr, val])

    def print_string(self, text):
        cstr = ir.Constant(ir.ArrayType(ir.IntType(8), len(text) + 1), bytearray(text.encode('utf8') + b'\0'))
        gv_name = f"str{len(self.module.global_values)}"
        global_str = ir.GlobalVariable(self.module, cstr.type, name=gv_name)
        global_str.linkage = 'internal'
        global_str.global_constant = True
        global_str.initializer = cstr

        ptr = self.builder.bitcast(global_str, ir.IntType(8).as_pointer())
        self.builder.call(self.printf, [ptr])

    def generate(self, node):
        if isinstance(node, list):
            last_val = None
            for stmt in node:
                last_val = self.generate(stmt)
            if not self.builder.block.is_terminated:
                self.builder.ret(ir.Constant(ir.IntType(32), 0))
            return last_val

        if isinstance(node, Number):
            return ir.Constant(ir.IntType(32), node.value)

        elif isinstance(node, StringLiteral):
            return node.value

        elif isinstance(node, BinOp):
            left = self.generate(node.left)
            right = self.generate(node.right)
            if node.op == "PLUS":
                return self.builder.add(left, right, name="addtmp")
            elif node.op == "MINUS":
                return self.builder.sub(left, right, name="subtmp")
            elif node.op == "TIMES":
                return self.builder.mul(left, right, name="multmp")
            elif node.op == "DIVIDE":
                return self.builder.sdiv(left, right, name="divtmp")
            else:
                raise Exception(f"Unknown operator {node.op}")

        elif isinstance(node, ArrayLiteral):
            elem_vals = [self.generate(e) for e in node.elements]
            array_type = ir.ArrayType(ir.IntType(32), len(elem_vals))
            arr_ptr = self.builder.alloca(array_type)
            zero = ir.Constant(ir.IntType(32), 0)
            for i, val in enumerate(elem_vals):
                idx = ir.Constant(ir.IntType(32), i)
                ptr = self.builder.gep(arr_ptr, [zero, idx])
                self.builder.store(val, ptr)
            return arr_ptr

        elif isinstance(node, ArrayAccess):
            arr_ptr = self.generate(node.array)
            if not isinstance(arr_ptr.type, ir.PointerType):
                temp_ptr = self.builder.alloca(arr_ptr.type)
                self.builder.store(arr_ptr, temp_ptr)
                arr_ptr = temp_ptr
            idx_val = self.generate(node.index)
            zero = ir.Constant(ir.IntType(32), 0)
            elem_ptr = self.builder.gep(arr_ptr, [zero, idx_val])
            return self.builder.load(elem_ptr)

        elif isinstance(node, Assign):
            if isinstance(node.value, ArrayLiteral):
                val_ptr = self.generate(node.value)
                self.variables[node.name] = val_ptr
                return val_ptr
            elif isinstance(node.name, ArrayAccess):
                arr_ptr = self.variables.get(node.name.array.name)
                if arr_ptr is None:
                    raise Exception(f"Undefined variable {node.name.array.name}")
                idx_val = self.generate(node.name.index)
                zero = ir.Constant(ir.IntType(32), 0)
                elem_ptr = self.builder.gep(arr_ptr, [zero, idx_val])
                val = self.generate(node.value)
                self.builder.store(val, elem_ptr)
                return val
            else:
                val = self.generate(node.value)
                ptr = self.builder.alloca(ir.IntType(32), name=node.name)
                self.builder.store(val, ptr)
                self.variables[node.name] = ptr
                return val

        elif isinstance(node, Var):
            ptr = self.variables.get(node.name)
            if ptr is None:
                raise Exception(f"Undefined variable {node.name}")
            return self.builder.load(ptr, name=node.name + "_load")

        elif isinstance(node, FunctionDef):
            func_type = ir.FunctionType(ir.IntType(32), [ir.IntType(32)] * len(node.params))
            func = ir.Function(self.module, func_type, name=node.name)
            self.functions[node.name] = func
            block = func.append_basic_block(name="entry")
            old_builder = self.builder
            old_vars = self.variables.copy()
            self.builder = ir.IRBuilder(block)
            self.variables = {}
            for i, arg in enumerate(func.args):
                arg.name = node.params[i]
                ptr = self.builder.alloca(ir.IntType(32), name=arg.name)
                self.builder.store(arg, ptr)
                self.variables[arg.name] = ptr
            for stmt in node.body:
                self.generate(stmt)
            if not self.builder.block.is_terminated:
                self.builder.ret(ir.Constant(ir.IntType(32), 0))
            self.builder = old_builder
            self.variables = old_vars
            return func

        elif isinstance(node, Return):
            ret_val = self.generate(node.value)
            self.print_int(ret_val)
            self.builder.ret(ret_val)
            return ret_val

        elif isinstance(node, FunctionCall):
            func = self.functions.get(node.name)
            if func is None:
                raise Exception(f"Undefined function {node.name}")
            args = [self.generate(arg) for arg in node.args]
            return self.builder.call(func, args, name="calltmp")

        elif isinstance(node, Print):
            if isinstance(node.value, StringLiteral):
                self.print_string(node.value.value)
            else:
                val = self.generate(node.value)
                self.print_int(val)
            return None

        elif isinstance(node, Input):
            var_ptr = self.builder.alloca(ir.IntType(32))
            fmt_ptr = self.builder.bitcast(self.fmt_str_scan, ir.IntType(8).as_pointer())
            self.builder.call(self.scanf, [fmt_ptr, var_ptr])
            return self.builder.load(var_ptr)

        else:
            raise Exception(f"Unsupported AST node type {type(node)}")

    def finish(self):
        if not self.builder.block.is_terminated:
            self.builder.ret(ir.Constant(ir.IntType(32), 0))
        return self.module
