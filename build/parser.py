from build.my_ast import Number, BinOp, Assign, Var, FunctionDef, FunctionCall, Return, Print, Input, StringLiteral, ArrayLiteral, ArrayAccess

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def peek(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def consume(self, expected_type=None):
        token = self.peek()
        if token is None:
            return None
        if expected_type and token[0] != expected_type:
            raise SyntaxError(f"Expected {expected_type}, found {token[0]}")
        self.pos += 1
        return token

    def parse_statement(self):
        tok = self.peek()
        if tok is None:
            return None

        if tok[0] == "FUNC":
            return self.parse_function()

        elif tok[0] == "RETURN":
            return self.parse_return()

        elif tok[0] == "PRINT":
            self.consume("PRINT")
            if self.peek() and self.peek()[0] == "STRING":
                value = self.consume("STRING")[1]
                return Print(StringLiteral(value))
            else:
                value = self.expr()
                return Print(value)

        elif tok[0] == "LBRACE":
            self.consume("LBRACE")
            statements = []
            while self.peek() and self.peek()[0] != "RBRACE":
                statements.append(self.parse_statement())
            self.consume("RBRACE")
            return statements

        elif tok[0] == "ID":
            if self.pos + 1 < len(self.tokens):
                next_tok = self.tokens[self.pos + 1]

                if next_tok[0] == "ASSIGN":
                    name = self.consume("ID")[1]
                    self.consume("ASSIGN")
                    value = self.expr()
                    return Assign(name, value)

                elif next_tok[0] == "LBRACKET":
                    current_pos = self.pos
                    array_name = self.consume("ID")[1]
                    self.consume("LBRACKET")
                    index = self.expr()
                    self.consume("RBRACKET")

                    if self.peek() and self.peek()[0] == "ASSIGN":
                        self.consume("ASSIGN")
                        value = self.expr()
                        return Assign(ArrayAccess(Var(array_name), index), value)
                    else:
                        self.pos = current_pos
                        return self.expr()
                else:
                    return self.expr()
            else:
                return self.expr()

        else:
            return self.expr()

    def parse(self):
        statements = []
        while True:
            if not self.peek():
                break
            stmt = self.parse_statement()
            if isinstance(stmt, list):
                statements.extend(stmt)
            else:
                statements.append(stmt)
        return statements

    def parse_function(self):
        self.consume("FUNC")
        name = self.consume("ID")[1]
        self.consume("LPAREN")
        params = []
        if self.peek() and self.peek()[0] != "RPAREN":
            params.append(self.consume("ID")[1])
            while self.peek() and self.peek()[0] == "COMMA":
                self.consume("COMMA")
                params.append(self.consume("ID")[1])
        self.consume("RPAREN")
        if self.peek() and self.peek()[0] == "LBRACE":
            body = self.parse_statement()
        else:
            body = []
        return FunctionDef(name, params, body)

    def parse_return(self):
        self.consume("RETURN")
        value = self.expr()
        return Return(value)

    def expr(self):
        node = self.term()
        while self.peek() and self.peek()[0] in ("PLUS", "MINUS"):
            op = self.consume()[0]
            right = self.term()
            node = BinOp(node, op, right)
        return node

    def term(self):
        node = self.factor()
        while self.peek() and self.peek()[0] in ("TIMES", "DIVIDE"):
            op = self.consume()[0]
            right = self.factor()
            node = BinOp(node, op, right)
        return node

    def factor(self):
        token = self.peek()

        if token[0] == "NUMBER":
            self.consume("NUMBER")
            return Number(token[1])

        elif token[0] == "STRING":
            value = self.consume("STRING")[1]
            return StringLiteral(value)

        elif token[0] == "LBRACKET":
            self.consume("LBRACKET")
            elements = []
            if self.peek()[0] != "RBRACKET":
                elements.append(self.expr())
                while self.peek() and self.peek()[0] == "COMMA":
                    self.consume("COMMA")
                    elements.append(self.expr())
            self.consume("RBRACKET")
            return ArrayLiteral(elements)

        elif token[0] == "ID":
            name = self.consume("ID")[1]
            if self.peek() and self.peek()[0] == "LBRACKET":
                self.consume("LBRACKET")
                index = self.expr()
                self.consume("RBRACKET")
                return ArrayAccess(Var(name), index)
            if name == "input" and self.peek() and self.peek()[0] == "LPAREN":
                self.consume("LPAREN")
                self.consume("RPAREN")
                return Input()
            elif self.peek() and self.peek()[0] == "LPAREN":
                self.consume("LPAREN")
                args = []
                if self.peek() and self.peek()[0] != "RPAREN":
                    args.append(self.expr())
                    while self.peek() and self.peek()[0] == "COMMA":
                        self.consume("COMMA")
                        args.append(self.expr())
                self.consume("RPAREN")
                return FunctionCall(name, args)
            else:
                return Var(name)

        elif token[0] == "LPAREN":
            self.consume("LPAREN")
            node = self.expr()
            self.consume("RPAREN")
            return node

        else:
            raise SyntaxError(f"Unexpected token: {token}")
