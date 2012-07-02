
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
    name = p[1]+'_'+str(len(VARIABLES))
    VARIABLES[name] = Variable(p[3],name,None)
    p[0] = p[3]

def p_vars_init(p):
    'varsinit : VAL IDENTIFIER EQUALS expression variables'
    VARIABLES[p[2]] = Variable(p[1],p[2],p[4])
    
def p_type(p):
    '''type : INT 
            | FLOAT 
            | BOOLEAN 
            | STRING 
            | LIST'''
    p[0] = p[1]

def p_expression(p):
    'expression : NUMBER SEMICOLON'
    p[0] = p[1]
    
def p_error(p):
    print("Syntax error at '%s'" % p.value)

import ply.yacc as yacc
YACC = yacc
YACC.yacc()
    



