#Crie um algoritimo que leia um número e mostre o seu dobro triplo e raiz quadrada.
n = int(input('Digite um numero: '))
print('O dobro do seu numero é {},o triplo do seu numero é {} e a raiz quadrada é {:.2f}'.format(n*2,n*3,pow(n,(1/2))))