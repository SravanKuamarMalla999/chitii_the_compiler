from build.lexer import tokenize
from build.parser import Parser
from build.codegen import CodeGen

def main():
    # Read source code from file
    with open("program.txt", "r") as f:
        source_code = f.read()

    # Tokenize source code
    tokens = tokenize(source_code)

    # Parse tokens into AST
    parser = Parser(tokens)
    ast = parser.parse()  # List of statements

    # Generate LLVM IR from AST
    codegen = CodeGen()
    codegen.generate(ast)
    llvm_ir = codegen.finish()

    # Print LLVM IR (optional)
    print(str(llvm_ir))

    # Write LLVM IR to file
    with open("program.ll", "w") as f:
        f.write(str(llvm_ir))

    print("LLVM IR generated and saved to program.ll")

if __name__ == "__main__":
    main()
