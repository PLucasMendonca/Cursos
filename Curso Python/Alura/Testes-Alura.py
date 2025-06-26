print("*" * 32)
print("Bem vindo ao jogo de Adivinhação")
print("*" * 32)

numero_secreto = 42
total_de_tentativas = 3

for rodada in range(1, total_de_tentativas + 1) :
  print(f"Tentativa {rodada} de {total_de_tentativas}")
  chute = int(input("Digite um número entre 1 e 100: "))

  if(chute < 1 or chute > 100):
    print("Você deve digitar um número entre 1 e 100!")
    continue
  acertou = numero_secreto == chute
  maior = chute > numero_secreto
  menor = chute < numero_secreto
  
  print("Você digitou ", chute)
    
  if (acertou):
      print("Voce acertou")
      break
  else:
      if(maior):
          print("Você errou! O seu chute foi maior do que o número secreto.")
      elif(menor):
          print("Você errou! O seu chute foi menor do que o número secreto.")
  
print("Fim de Jogo")