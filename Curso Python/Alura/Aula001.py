import random
print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = random.randint(1,100)
total_de_tentativas = 0
pontos = 1000


print("Qual nível de dificuldade?")
print(" (1) Facil\n (2) Médio\n (3) Difícil")
print(numero_secreto)

nivel = int(input("Define o nível: "))
if(nivel == 1):
  total_de_tentativas = 20
elif(nivel ==2):
  total_de_tentativas = 10
else:
  total_de_tentativas = 5

for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("Digite um número entre 1 e 100: ")
    print("Você digitou " , chute_str)
    chute = int(chute_str)

    if(chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100!")
        continue

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if(acertou):
        print(f"Você acertou e fez {pontos} pontos !!")
        break
    else:
        if(maior):
          print("Você errou! O seu chute foi maior do que o número secreto.")
        elif(menor):
          print("Você errou! O seu chute foi menor do que o número secreto.")
          pontos_perdidos = abs(numero_secreto - chute)
          pontos = pontos - pontos_perdidos
print(f"O número secreto era {numero_secreto}. Você fez {pontos} pontos.")
print("Fim do jogo")