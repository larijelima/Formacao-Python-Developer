''' 
============ OBJETIVO DO PROJETO ============
Criar sistema bancário com as seguintes operações:
- DEPÓSITO (apenas valores positivos)
- SAQUE (com limite de R$500,00 por saque e máximo de três operações)
- EXTRATO (contendo todas as movimentações)
'''


saldo = 0
limite = 500
numero_saques = 0
limite_saques = 3
extrato = ""

while True:
  decisão = input("""
                  ============== MENU ==============
      QUAL AÇÃO DESEJA TOMAR?
      Depósito, digite d
      Saques, digite s
      Extrato, digite e
      Sair, digite x
      
      Digite sua opção:
      """
      )
 
  if decisão == 'd':
    valor = float(input("Informe valor para depósito: "))
    if valor > 0:
      saldo += valor
      extrato += f"Depósito: R$ {valor:.2f}\n"
      print(f'Depósito concluído no valor de R$ {valor:.2f}')
    else:
      print('Erro! Tente novamente')

  elif decisão == 's' and numero_saques < limite_saques:
    valor = float(input("Informe valor para saque: "))
    if valor > saldo:
      print("Você não possui saldo suficiente")
  
    elif valor > limite:
      print("O valor escolhido excede limite disponível")
  
    elif valor > 0:
      saldo -= valor
      print(f'Saque concluído no valor de R$ {valor}')
      extrato += f"Saque: R$ {valor:.2f}\n"
      numero_saques += 1
  
    else:
      print("Falha na operação. Tente novamente")
    
  elif decisão == 'e':
    print("================= EXTRATO ================= ")
    print(f'Saldo Atual = {saldo}')
    print("================= HISTÓRICO DE MOVIMENTAÇÕES ================= ")
    if extrato == "":
      print("Não houve movimentações")
    else:
      print(extrato)

  elif decisão == 'x':
    break
  
  else:
    print("Digite sua opção novamente")
