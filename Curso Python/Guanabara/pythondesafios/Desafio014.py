#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
c = float(input('Digite a temperatura em graus Celsius para sabermos quanto é em Fahrenheit:'))
f = 9 * c / 5 + 32
print('A temperatura de {}°C corresponde a {}F°'.format(c,f))
