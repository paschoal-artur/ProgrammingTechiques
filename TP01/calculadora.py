acumulador = 0

def soma(operando_a, operando_b):
    if operando_a is None:
        return acumulador + operando_b
    elif operando_b is None:
        return acumulador + operando_a
    return operando_a + operando_b

def subtracao(operando_a, operando_b):
    if operando_a is None:
        return acumulador - operando_b
    elif operando_b is None:
        return acumulador - operando_a
    return operando_a - operando_b

def multiplicacao(operando_a, operando_b):
    if operando_a is None:
        return acumulador * operando_b
    elif operando_b is None:
        return acumulador * operando_a 
    return operando_a * operando_b

def divisao(operando_a, operando_b):
    if operando_a is None:
        return acumulador / operando_b
    elif operando_b is None:
        return acumulador / operando_a
    return operando_a/operando_b

def memoria (resultado):
    global acumulador
    acumulador = resultado
