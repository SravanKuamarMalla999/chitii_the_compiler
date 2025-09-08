import re

TOKEN_SPECIFICATION = [
    ('COMMENT', r'#.*'),          # Comment from # to end of line
    ('PRINT',   r'\bprint\b'),   # print keyword with word boundaries
    ('RETURN',  r'\breturn\b'),
    ('FUNC',    r'\bfunc\b'),
    ('STRING',  r'"[^"]*"'),      # String literals
    ('NUMBER',  r'\d+'),          # Integer literals
    ('ID',      r'[A-Za-z_][A-Za-z0-9_]*'),  # Identifiers
    ('ASSIGN',  r'='),
    ('PLUS',    r'\+'),
    ('MINUS',   r'-'),
    ('TIMES',   r'\*'),
    ('DIVIDE',  r'/'),
    ('LPAREN',  r'\('),
    ('RPAREN',  r'\)'),
    ('LBRACE',  r'\{'),
    ('RBRACE',  r'\}'),
    ('LBRACKET', r'\['),
    ('RBRACKET', r'\]'),
    ('COMMA',   r','),
    ('SEMICOLON', r';'),
    ('SKIP',    r'[ \t]+'),
    ('NEWLINE', r'\n'),
    ('MISMATCH',r'.'),
]

master_regex = '|'.join(f'(?P<{name}>{regex})' for name, regex in TOKEN_SPECIFICATION)
get_token = re.compile(master_regex).match

def tokenize(code):
    pos = 0
    tokens = []
    while pos < len(code):
        match = get_token(code, pos)
        if not match:
            raise SyntaxError(f'Unexpected character: {code[pos]}')
        kind = match.lastgroup
        value = match.group(kind)
        if kind == "COMMENT":
            pos = match.end()
            continue
        if kind == "STRING":
            value = value[1:-1]
        if kind == "SKIP" or kind == "NEWLINE":
            pos = match.end()
            continue
        if kind == "MISMATCH":
            raise SyntaxError(f'Unexpected token: {value}')
        tokens.append((kind, value))
        pos = match.end()
    return tokens
