
tokens = (
    'NUMBER','PLUS','MINUS','TIMES','DIVIDE','EQUALS','LPAREN','RPAREN',
    'VARIABLES_DECL','COLON', 'SEMICOLON', 'COMMA', 'VAL',
    'INT','FLOAT','BOOLEAN','STRING','LIST', 'CHAR', 'TRUE', 'FALSE',
    'IF','ELSE','IDENTIFIER'
    )

t_VARIABLES_DECL = r'Variables'
t_PLUS           = r'\+'
t_MINUS          = r'\*'
t_DIVIDE         = r'/'
t_EQUALS         = r'='
t_LPAREN         = r'\('
t_RPAREN         = r'\)'
t_COLON          = r'\:'
t_SEMICOLON      = r'\;'
t_COMMA          = r'\,'
t_INT            = r'int'
t_FLOAT          = r'float'
t_BOOLEAN        = r'boolean'
t_STRING         = r'string'
t_LIST           = r'list'
t_CHAR           = r'char'
t_TRUE           = r'True'
t_FALSE          = r'False'
t_IF             = r'if'
t_ELSE           = r'else'
t_VAL            = r'val'
t_IDENTIFIER     = r'bruno'#[a-zA-Z_][a-zA-Z0-9_]*'

t_ignore         = " \t"

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





