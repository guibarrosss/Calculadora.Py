def calculadora_meta_financeira():
  #Solicita ao usuário a meta financeira
  meta_financeira = float(input("Digite a sua meta financeira: R$ "))

  #Solicita ao usuário a economia mensal
  economia_mensal = float(input("Digite a economia mensal: R$ "))

  #Verifica se a economia mensal é maior que zero
  if economia_mensal <= 0:
      print("A economia mensal deve ser maior que zero.")
      return

  #Calcula o tempo necessário para atingir a meta
  meses_necessarios = meta_financeira / economia_mensal

  #Calcula anos e meses a partir dos meses necessários
  anos = int(meses_necessarios // 12)
  meses = int(meses_necessarios % 12)

  #Exibe o resultado
  if anos == 0:
      print(f"Você levará {meses} meses para atingir a meta de R$ {meta_financeira:.2f}.")
  else:
      print(f"Você levará {anos} anos e {meses} meses para atingir a meta de R$ {meta_financeira:.2f}.")

#Chama a função da calculadora
calculadora_meta_financeira()