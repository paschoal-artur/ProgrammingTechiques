#criar classe
class Calculadora:
    def __init__(self):
        pass

    def memoria(self):
        global acumulador
        acumulador = 0
        return acumulador

    def soma(self, operando_a, operando_b):
        if operando_a is None:
            soma_a = operando_b + self.acumulador
            self.acumulador = soma_a 
            return soma_a 
        else:     
            return operando_a + operando_b
    def subtracao(self, operando_a, operando_b):
        if operando_a == 0:
            subtracao_a = operando_b - self.acumulador
            self.acumulador = subtracao_a
            return subtracao_a
        else:
            return operando_a - operando_b
    def multiplicacao(self, operando_a, operando_b):
        if operando_a == 0:
            multiplicacao_a = operando_b * self.acumulador
            self.acumulador = multiplicacao_a
            return multiplicacao_a
        else:
            return operando_a * operando_b
    def divisao(self, operando_a, operando_b):
        if operando_a == 0:
            divisao_a = operando_b / acumulador
            self.acumulador = divisao_a
            return divisao_a
        else:
            return operando_a / operando_b

