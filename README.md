Chitii The Compiler

A simple yet powerful compiler project built in Python, designed to transform source code into LLVM IR through lexical analysis, parsing, AST generation, and code generation. This project demonstrates the core concepts of compiler design step by step.

Features

Lexical Analysis → Tokenizes the source code

Parsing → Builds an Abstract Syntax Tree (AST)

Code Generation → Translates AST into LLVM Intermediate Representation (IR)

Modular Design → Separate modules for Lexer, Parser, and CodeGen

Extensible → Easy to add new language features

Project Structure
chitii_the_compiler/
│── build/              # Core compiler modules
│   ├── lexer.py        # Lexical analyzer
│   ├── parser.py       # Parser
│   ├── codegen.py      # LLVM code generator
│── examples/           # Example programs to test
│── main.py             # Entry point for compiler
│── requirements.txt    # Python dependencies
│── README.md           # Project documentation

Getting Started
1. Clone the Repository
git clone https://github.com/SravanKuamarMalla999/chitii_the_compiler.git
cd chitii_the_compiler

2. Install Dependencies
pip install -r requirements.txt

3. Run the Compiler
python main.py

Example Usage

Input program:

x = 42 + 3


Output tokens:

Tokens: [('ID', 'x'), ('ASSIGN', '='), ('NUMBER', '42'), ('PLUS', '+'), ('NUMBER', '3')]


Generated AST:

AST: Assign(x, Add(Number(42), Number(3)))


LLVM IR Output:

@x = global i32 0
define i32 @main() {
  store i32 45, i32* @x
  ret i32 0
}

Contributing

Contributions are welcome. Feel free to fork the repo, make changes, and submit a pull request.

License

This project is licensed under the MIT License – see the LICENSE
 file for details.

Author

Malla Sravan Kumar
Email: sravankumarmalla999@gmail.com

LinkedIn: https://www.linkedin.com/in/sravankumar-malla
