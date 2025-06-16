LIMITE_SAQUE = 3
saldo = 0
saques_realizados = 0
menu = '''
================
    Banco V1
================

Selecione uma opção:
[d] Depósito
[s] Saque
[e] Exibir extrato
[f] Finalizar e sair
'''

extrato = ""


while True:
    print(menu)
    opc = input(">> ")

    match(opc.lower()):
        case "d":
            depo = int(input("\nInforme o valor a ser depositado na conta: R$ "))
            while depo < 0:
                depo = int(input("\nValor inválido! Insira o valor correto a ser depositado na conta: R$ "))
            
            saldo += depo
            extrato += f"\nDepósito: R$ {depo}"
            print("Operação realizada com sucesso!\n")
        case "s":
            if saldo == 0:
                print("Não há dinheiro na conta!")
            elif saques_realizados == 3:
                print("Limite de saques atingido! Tente novamente amanhã!")
            else:
                saque = int(input("\nInforme o valor a ser sacado da conta: R$ "))
                while saque < 0:
                    saque = int(input("\nValor inválido! Insira o valor correto a ser sacado da conta: R$ "))
                
                if saque > 500:
                    print("Valor de saque supera limite de R$ 500")
                elif saque > saldo:
                    print("Valor de saque supera saldo disponível")
                else:
                    saldo -= saque
                    extrato += f"\nSaque: R$ {saque}"
                    saques_realizados += 1
                    print("Operação realizada com sucesso!\n")

        case "e":
            print('''
================
    Banco V1
================''')
            print("Extrato da conta:")
            print(f"Saldo: R$ {saldo:.2f}")
            print("Não houve movimentações na conta." if not extrato else extrato) 
            print()

        case "f":
            print("Finalizando operações!")
            break

        case _:
            print("Insira uma opção válida")