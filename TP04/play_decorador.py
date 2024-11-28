
def dividir(a, b):
    return a / b

def divisao_inteligente(dividir):
    def wrapper(a, b):
        if b == 0:
            return "Não é possível dividir por zero"
        return dividir(a, b)
    return wrapper

if __name__ == "__main__":
    dividir = divisao_inteligente(dividir)
    print(dividir(10, 0))
    print(dividir(10, 2))