from calculadora_oo import Calculadora

def test_calculadora(operando_a, operando_b):
    calculadora = Calculadora()
    print(calculadora.soma(operando_a, operando_b))
    print(calculadora.subtracao(operando_a, operando_b))
    print(calculadora.multiplicacao(operando_a, operando_b))
    print(calculadora.divisao(operando_a, operando_b)) 

test_calculadora(0,2)
#test_calculadora(2,0)
#test_calculadora(2,2)

