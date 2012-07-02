
tokens = (
    'NUMBER','PLUS','MINUS','TIMES','DIVIDE','EQUALS','LPAREN','RPAREN',
    'VARIABLES_DECL','IDENTIFIER'
    )

t_VARIABLES_DECL = r'Variables'
t_PLUS           = r'\+'
t_MINUS          = r'\*'
t_DIVIDE         = r'/'
t_EQUALS         = r'='
t_LPAREN         = r'\('
t_RPAREN         = r'\)'
t_IDENTIFIER     = r'[a-zA-Z_][a-zA-Z0-9_]*'


t_ignore " \t"

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)





