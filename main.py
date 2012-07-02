from tokens import LEX,YACC,VARIABLES

def main():
    entry = "Variables \
             bruno,bruno,bruno:int; \
             val bruno = 5;"
    LEX.input(entry)
    for tok in iter(LEX.token, None):
        print("%s %s" % (tok.type,tok.value))
    print('\n\n')
    
    YACC.parse(entry)
    
    for v in VARIABLES:
        print(VARIABLES[v])
    

if __name__ == "__main__":
    main()
