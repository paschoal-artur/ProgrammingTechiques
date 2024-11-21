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

    def render_juros(self, taxa:float)->None:
        self.creditar(self.get_saldo() * taxa)


class Banco:

    def __init__(self, taxa: float):
        self.__contas = []
        self.__taxa = taxa

    def cadastrar(self, conta:Conta)->None:
        self.__contas.append(conta)

    def procurar(self, numero:str)-> Conta:
        self.__contas = [conta for conta in self.__contas if conta.get_numero() == numero]

    def creditar (self, numero:str ,valor:float) -> None :
        self.__numero = [conta.creditar(valor) for conta in self.__contas if conta.get_numero() == numero]

    def debitar(self, numero:str, valor:float) -> None:
        self.__debitar = [conta.debitar(valor) for conta in self.__contas if conta.get_numero() == numero]

    def saldo(self, numero:str) -> float:
        self.__numero = [conta.get_saldo() for conta in self.__contas if conta.get_numero() == numero]

    def transferir (self, origem:str, destino:str, valor:float) -> None:
        self.__origem = [conta.debitar(valor) for conta in self.__contas if conta.get_numero() == origem]
    
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

