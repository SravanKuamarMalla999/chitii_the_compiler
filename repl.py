from build.lexer import tokenize
from build.parser import Parser
from build.codegen import CodeGen
from llvmlite import binding
import ctypes

def compile_and_run(source_code):
    tokens = tokenize(source_code)
    parser = Parser(tokens)
    ast = parser.parse()

    codegen = CodeGen()
    codegen.generate(ast)
    llvm_ir = codegen.finish()

    binding.initialize()
    binding.initialize_native_target()
    binding.initialize_native_asmprinter()

    target = binding.Target.from_default_triple()
    target_machine = target.create_target_machine()

    backing_mod = binding.parse_assembly("")
    engine = binding.create_mcjit_compiler(backing_mod, target_machine)

    mod = binding.parse_assembly(str(llvm_ir))
    mod.verify()

    engine.add_module(mod)
    engine.finalize_object()

    func_ptr = engine.get_function_address("main")
    cfunc = ctypes.CFUNCTYPE(ctypes.c_int)(func_ptr)

    return cfunc()

def repl():
    print("Welcome to chitii_the_compiler REPL! Type 'exit' to quit.")
    while True:
        try:
            code = input('>>> ')
            if code.strip().lower() == "exit":
                break
            result = compile_and_run(code)
            print("Result:", result)
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    repl()
