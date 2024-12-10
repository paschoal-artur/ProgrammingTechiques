#criar classe
class Conta:
    def __init__(self, numero:str):
        self.__numero = numero 
        self.__saldo = 0.0

    def creditar(self, valor:float)->None:
        self.__saldo += valor

    def debitar(self, valor:float)->None:
        self.__saldo -= valor

    def get_numero(self)->str:
        return self.__numero
    
    def get_saldo(self)->float:
        return self.__saldo 

class Banco:
    def __init__(self):
        self.__contas = []

    def cadastrar(self, conta:Conta)->None:
        self.__contas.append(conta)

    def procurar(self, numero:str)-> Conta:
        for i in self.__contas:
            if i.get_numero() == numero:
                return i 

    def creditar (self, numero:str ,valor:float) -> None :
        self.procurar(numero).creditar(valor)

    def debitar(self, numero:str, valor:float) -> None:
        self.procurar(numero).debitar(valor)

    def saldo(self, numero:str) -> float:
        return self.procurar(numero).get_saldo()

    def transferir (self, origem:str, destino:str, valor:float) -> None:
        self.procurar(origem).debitar(valor)
        self.procurar(destino).creditar(valor) 
