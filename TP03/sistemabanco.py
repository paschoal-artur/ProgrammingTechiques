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

class ContaEspecial(Conta):
    def __init__(self, numero: str):
        super() .__init__(numero)
        self.__bonus = 0
    
    def render_bonus(self)->None:
        self.creditar(self.__bonus)
    
    def creditar(self, valor:float)->None:
        self.__bonus += valor * 0.01
        super().creditar(valor)


class ContaPoupança(Conta):
    def __init__(self, numero:str):
        super().__init__(numero)

    def render_juros(self, taxa:float) -> None:
        self.creditar(self.get_saldo() * taxa)

class Banco:

    def __init__(self, taxa: float):
        self.__contas = []
        self.__taxa = taxa

    def cadastrar(self, conta:Conta)->None:
        self.__contas.append(conta)

    def procurar(self, numero:str)-> Conta:
        for conta in self.__contas:
            if conta.get_numer() == numero:
                return conta
        return None 

    def creditar (self, numero:str ,valor:float) -> None :
        for conta in self.__contas:
            if conta.get_numero() == numero:
                conta.creditar(valor)
                return  

    def debitar(self, numero:str, valor:float) -> None:
        for conta in self.__contas:
            if conta.get_numero() == numero:
                conta.debitar(valor)
                return 

    def saldo(self, numero:str) -> float:
        for conta in self.__contas:
            if conta.get_numero() == numero:
                return conta.get_saldo()

    def transferir (self, origem:str, destino:str, valor:float) -> None:
        conta_origem = None 
        conta_destino = None
        for conta in self.__contas:
            if conta.get_numero() == origem:
                conta_origem = conta
            if conta.get_numero() == destino:
                conta_destino = conta
        if conta_origem and conta_destino:
            conta_origem.debitar(valor)
            conta_destino.creditar(valor)

    def render_juros(self, numero: str, taxa: float) -> None:
        conta = self.procurar(numero)
        if isinstance(conta, ContaPoupança):
            conta.render_juros(taxa)

    def render_bonus(self, numero:str) -> None:
        conta = self.procurar(numero)
        if isinstance(conta, ContaEspecial):
            conta.render_bonus()
    
    def get_taxa(self)->float:
        return self.__taxa

    def set_taxa(self, taxa:float) -> None:
        self.__taxa = taxa

