menu = """

[d] Depositar
[s] Sacar 
[e] Extrato 
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    
    if opcao == "d":
        valor_deposito = float(input("Deposite aqui o valor desejado: "))
        
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
            
        else:
            print("Valor inválido, tente novamente.")    
    
    elif opcao == "s":
        valor = float(input("Informe valor do saque: "))
        
        saldo_excedido = valor > saldo
        
        limite_excedido = valor > limite
        
        saque_excedido = numero_saques >= LIMITE_SAQUES
        
        if saldo_excedido:
            print("Você não tem mais $ suficiente!")
        
        elif limite_excedido:
            print("Você já excedeu o limite!")  
        
        elif saque_excedido:
            print("Você já fez o máximo de saques!")  
            
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1       
        
        else:
            print("O valor informado é inválido.")
            
    elif opcao ==  "e":
        print("\n¨¨¨¨¨¨¨¨ EXTRATO ¨¨¨¨¨¨")
        print("Sem movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:;2f}")
        print("¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨") 
        
    elif opcao == 'q':
        break  
       
     
                







 