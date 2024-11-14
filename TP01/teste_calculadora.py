import calculadora as calc 

def teste_quest1(a, b):
    print(calc.soma(a,b))
    print(calc.subtracao(a,b))
    print(calc.multiplicacao(a,b))
    print(calc.divisao(a,b))

def teste_quest2(a,b):
    #operando b faltando
    print(calc.soma(a,Null))
    print(calc.subtracao(a,Null))
    print(calc.multiplicacao(a,Null))
    print(calc.divisao(a,Null))

    #operando a faltando
    print(calc.soma(Null,b))
    print(calc.subtracao(Null,b))
    print(calc.multiplicacao(Null,b))
    print(calc.divisao(Null,b))

teste_quest1(1,None)