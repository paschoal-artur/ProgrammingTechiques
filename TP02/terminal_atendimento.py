from sisbanco import Conta, Banco 

def terminal():
    sisbanco = Banco()
    while(True):
        print("SisBanco::Bem vindo! ")
        print(".::Opcoes::. ")
        print("[0]-Criar Conta ")
        print("[1]-Creditar ")
        print("[2]-Debitar ")
        print("[3]-Transferir ")
        print("[4]-Saldo ")
        print("[5]-Sair ")
        opcao = input("Digite a opcao: ")

        if opcao == 0:
            num_conta = input("Digite o numero da conta a ser criada: ")
            conta = Conta(num_conta)
            sisbanco.cadastrar(conta)
        elif opcao == 1:
            num_conta  = input("Digite o numero da conta:")
            conta = sisbanco.procurar(num_conta)
            if conta == None:
                print("Conta nao encontrada")
                break
            valor = float(input("Digite o valor a ser creditado: "))
            sisbanco.creditar(num_conta, valor)
        elif opcao == 2:
            num_conta  = input("Digite o numero da conta:")
            conta = sisbanco.procurar(num_conta)
            if conta == None:
                print("Conta nao encontrada")
                break
            valor = float(input("Digite o valor a ser debitado: "))
            sisbanco.debitar(num_conta, valor)
        elif opcao == 3:
            num_conta_origem  = input("Digite o numero da conta de origem:")
            conta_origem = sisbanco.procurar(num_conta_origem)
            if conta_origem == None:
                print("Conta nao encontrada")
                break
            num_conta_destino = input("Digite o numero da conta de destino:")
            conta_destino = sisbanco.procurar(num_conta_destino)
            if conta_destino == None:
                print("Conta nao encontrada")
                break 
            valor = float(input("Digite o valor a ser transferido: "))
            sisbanco.transferir(num_conta_origem, num_conta_destino, valor)
        elif opcao == 4:

if __name__ == "__main__":
    terminal()