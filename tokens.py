
tokens = (
    'PLUS','MINUS','TIMES','DIVIDE','EQUALS','LPAREN','RPAREN',
    'VARIABLES_DECL','COLON', 'SEMICOLON', 'COMMA', 'VAL',
    'INT','FLOAT','BOOLEAN','STRING', 'CHAR', 'TRUE', 'FALSE',
    'IF','ELSE','IDENTIFIER','TYPE'
    )

t_PLUS           = r'\+'
t_MINUS          = r'\*'
t_DIVIDE         = r'/'
t_EQUALS         = r'='
t_LPAREN         = r'\('
t_RPAREN         = r'\)'
t_COLON          = r'\:'
t_SEMICOLON      = r'\;'
t_COMMA          = r'\,'

t_ignore         = " \t"

def t_VARIABLES_DECL(t):
    r'Variables'
    return t
def t_VAL(t):
    r'val'
    return t
def t_IF(t):
    r'if'
    return t
def t_ELSE(t):
    r'else'
    return t

def t_FLOAT(t):
    r'-?\d+\.\d*(e-?\d+)?'
    t.value = float(t.value)
    return t
def t_INT(t):
    r'-?\d+'
    t.value = int(t.value)
    return t
def t_BOOLEAN(t):
    r'true|false'
    return t
def t_STRING(t):
    r'\"([^\\"]|(\\.))*\"'
    escaped = 0
    str = t.value[1:-1]
    new_str = ""
    for i in range(0, len(str)):
        c = str[i]
        if escaped:
            if c == "n":
                c = "\n"
            elif c == "t":
                c = "\t"
            new_str += c
            escaped = 0
        else:
            if c == "\\":
                escaped = 1
            else:
                new_str += c
    t.value = new_str
    return t
def t_CHAR(t):
    r'\'.?\''
    t.value = t.value[1:-1]
    return t

def t_TYPE(t):
    r'int|float|boolean|string|char'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

import ply.lex as lex
LEX = lex
LEX.lex()

class Variable(object):
    def __init__(self,type_,name,value):
        self.type = type_
        self.name = name
        self.value = value
    
    def __str__(self):
        return '%s %s = %s' % (self.type,self.name,self.value)

class AlreadyDeclaredError(Exception):
    def __init__(self,msg):
        Exception.__init__(self,msg)

VARIABLES = {}

def p_vars_decl_start(p):
    'variables : VARIABLES_DECL variables'
    pass

def p_vars(p):
    '''variables : varsnoinit
                 | varsinit
                 | '''
    
def p_vars_noinit(p):
    '''varsnoinit : IDENTIFIER COMMA varsnoinit
                  | IDENTIFIER COLON type SEMICOLON variables'''
    name = p[1]
    if name in VARIABLES:
        raise AlreadyDeclaredError('Variable %s declared more than once.' % (name))
    
    VARIABLES[name] = Variable(p[3],name,None)
    p[0] = p[3]

def p_vars_init(p):
    'varsinit : VAL IDENTIFIER EQUALS expression variables'
    VARIABLES[p[2]] = Variable(p[1],p[2],p[4])
    
def p_type(p):
    'type : TYPE'
    p[0] = p[1]

def p_expression(p):
    '''expression : typevalue SEMICOLON'''
    p[0] = p[1]

def p_typevalue(p):
    '''typevalue : INT 
                 | FLOAT
                 | STRING
                 | CHAR
                 | BOOLEAN
                 | listvalue'''
    p[0] = p[1]                  

def p_list_start(p):
    'listvalue : LPAREN list_aux_1 RPAREN'
    p[0] = p[2]
    
def p_list_aux_1(p):
    '''list_aux_1 : typevalue list_aux_2
                  | '''
    p[0] = []
    try:
        p[0].append(p[1])
        p[0] += p[2]
    except Exception as e:
        pass
def p_list_aux_2(p):
    '''list_aux_2 : COMMA list_aux_1
                  | '''
    try:
        p[0] = p[2]
    except Exception as e:
        pass
def p_error(p):
    print("Syntax error at '%s'" % p.value)

import ply.yacc as yacc
YACC = yacc
YACC.yacc()
    



