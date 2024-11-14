from matematica import aritmetica, geometria

def teste_aritmetica(a, b):
    print(aritmetica.soma(a, b))
    print(aritmetica.subtracao(a, b))

def teste_circulo(r):
    print(geometria.area_circulo(r))

def teste_retangulo(a, b):
    print(geometria.area_retangulo(a, b))

teste_aritmetica(2, 5)
teste_circulo(5)
teste_retangulo(2,5)