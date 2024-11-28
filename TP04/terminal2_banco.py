from sisbanco2 import Banco, Conta, ContaPoupanca, ContaEspecial, ContaImposto

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
        print("[5]-Render Juros ")
        print("[6]-Render Bonus ")
        print("[7]-Alterar Taxa_Juros ")
        print("[8]-Alterar Taxa Imposto ")
        print("[9]-Sair ")

        opcao = int(input("Digite a opcao: "))

        if opcao == 0:
            num_conta = input("Digite o numero da conta a ser criada: ")
            print('[0] para conta normal')
            print('[1] para conta especial')
            print('[2] para conta poupança') 
            print('[3] para conta com imposto')
            tipo_conta = int(input("Digite o tipo da conta a ser criado: "))

            if tipo_conta == 1:
                conta = ContaEspecial(num_conta)
            elif tipo_conta == 2:  
                conta = ContaPoupanca(num_conta)
            elif tipo_conta == 3:
                conta = ContaImposto(num_conta)
            else:
                conta = Conta(num_conta)
            sisbanco.cadastrar(conta)
            print(f'Conta {num_conta} cadastrada com sucesso! ')

        elif opcao == 1:
            num_conta  = input("Digite o numero da conta:")
            conta = sisbanco.procurar(num_conta)
            if conta == None:
                print("Conta nao encontrada")
                continue
            valor = float(input("Digite o valor a ser creditado: "))
            sisbanco.creditar(num_conta, valor)
            print(f'Valor {valor} creditado com sucesso na conta {num_conta}! ')

        elif opcao == 2:
            num_conta  = input("Digite o numero da conta:")
            conta = sisbanco.procurar(num_conta)
            if conta == None:
                print("Conta nao encontrada")
                continue
            valor = float(input("Digite o valor a ser debitado: "))
            sisbanco.debitar(num_conta, valor)
            print(f'Valor: {valor} debitado com sucesso na conta {num_conta}! ')

        elif opcao == 3:
            num_conta_origem  = input("Digite o numero da conta de origem:")
            conta_origem = sisbanco.procurar(num_conta_origem)
            if conta_origem == None:
                print("Conta nao encontrada")
                continue
            num_conta_destino = input("Digite o numero da conta de destino:")
            conta_destino = sisbanco.procurar(num_conta_destino)
            if conta_destino == None:
                print("Conta nao encontrada")
                continue 
            valor = float(input("Digite o valor a ser transferido: "))
            sisbanco.transferir(num_conta_origem, num_conta_destino, valor)
            print(f"Transferência de {valor} realizada com sucesso de {num_conta_origem} para {num_conta_destino}")

        elif opcao == 4:
            num_conta  = input("Digite o numero da conta:")
            conta = sisbanco.procurar(num_conta)
            if conta == None:
                print("Conta nao encontrada")
                continue
            print(f"Saldo da conta {num_conta}: {sisbanco.saldo(num_conta)}")

        elif opcao == 5:
            num_conta  = input("Digite o numero da conta:")
            conta = sisbanco.procurar(num_conta)
            if conta == None:
                print("Conta nao encontrada")
                continue 
            taxa = float(input("Digite a taxa de juros: "))
            conta.render_juros(taxa)
            print(f"Juros de {taxa} renderizados com sucesso na conta {num_conta}!")

        elif opcao == 6:
            num_conta  = input("Digite o numero da conta:")
            conta = sisbanco.procurar(num_conta)
            if conta == None:
                print("Conta nao encontrada")
                continue
            conta.render_bonus()
            print(f"Bonus renderizado com sucesso na conta {num_conta}!")

        elif opcao == 7:
            taxa_juros = float(input("Digite a nova taxa de juros: "))
            sisbanco.set_taxa_poupanca(taxa_juros)
            print(f"Taxa de juros de poupanca alterada para {taxa_juros}")

        elif opcao == 8:
            taxa_imposto = float(input("Digite a nova taxa de imposto:"))
            sisbanco.set_taxa_imposto(taxa_imposto)
            print(f"Taxa de imposto alterada para {taxa_imposto}")
        
        elif opcao == 9:
            print("Até logo!")
            break 

if __name__ == "__main__":
    terminal()