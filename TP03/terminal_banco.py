from sistemabanco import Banco, Conta, ContaPoupança, ContaEspecial

def terminal():
    sisbanco = Banco(taxa = 0.01)
    while(True):
        print("SisBanco::Bem vindo! ")
        print(".::Opcoes::. ")
        print("[0]-Criar Conta ")
        print("[1]-Creditar ")
        print("[2]-Debitar ")
        print("[3]-Transferir ")
        print("[4]-Saldo ")
        print("[5]-Render Juros ")
        print("[6]-Render Bonus ")
        print("[7]-Alterar Taxa ")
        print("[8]-Sair ")
        opcao = int(input("Digite a opcao: "))

        if opcao == 0:
            num_conta = input("Digite o numero da conta a ser criada: ")
            print('[0] para conta normal')
            print('[1] para conta especial')
            print('[2] para conta poupança') 
            tipo_conta = int(input("Digite o tipo da conta a ser criado: "))

            if tipo_conta == 1:
                conta = ContaPoupança(num_conta)
            elif tipo_conta == 2:  
                conta = ContaEspecial(num_conta)
            else:
                conta = Conta(num_conta)

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
            num_conta  = input("Digite o numero da conta:")
            conta = sisbanco.procurar(num_conta)
            if conta == None:
                print("Conta nao encontrada")
                break
            print("Saldo: ", sisbanco.saldo(num_conta))

        elif opcao == 5:
            num_conta  = input("Digite o numero da conta:")
            if conta == None:
                print("Conta nao encontrada")
                break
            taxa = float(input("Digite a taxa de juros: "))
            conta.render_juros(taxa)

        elif opcao == 6:
            num_conta  = input("Digite o numero da conta:")
            if conta == None:
                print("Conta nao encontrada")
                break
            conta.render_bonus()

        elif opcao == 7:
            taxa = float(input("Digite a nova taxa de juros: "))
            sisbanco.set_taxa(taxa)

        elif opcao == 8:
            break

if __name__ == "__main__":
    terminal()