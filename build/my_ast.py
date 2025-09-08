class ASTNode:
    pass

class Number(ASTNode):
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return f"Number({self.value})"

class StringLiteral(ASTNode):
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return f'StringLiteral("{self.value}")'

class BinOp(ASTNode):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right
    def __repr__(self):
        return f"BinOp({self.left}, '{self.op}', {self.right})"

class Assign(ASTNode):
    def __init__(self, name, value):
        self.name = name
        self.value = value
    def __repr__(self):
        return f"Assign({self.name}, {self.value})"

class Var(ASTNode):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f"Var({self.name})"

class FunctionDef(ASTNode):
    def __init__(self, name, params, body):
        self.name = name
        self.params = params
        self.body = body
    def __repr__(self):
        return f"FunctionDef({self.name}, params={self.params}, body={self.body})"

class FunctionCall(ASTNode):
    def __init__(self, name, args):
        self.name = name
        self.args = args
    def __repr__(self):
        return f"FunctionCall({self.name}, args={self.args})"

class Return(ASTNode):
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return f"Return({self.value})"

class Print(ASTNode):
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return f"Print({self.value})"

class Input(ASTNode):
    def __repr__(self):
        return "Input()"

class ArrayLiteral(ASTNode):
    def __init__(self, elements):
        self.elements = elements
    def __repr__(self):
        return f"ArrayLiteral({self.elements})"

class ArrayAccess(ASTNode):
    def __init__(self, array, index):
        self.array = array
        self.index = index
    def __repr__(self):
        return f"ArrayAccess({self.array}, {self.index})"
