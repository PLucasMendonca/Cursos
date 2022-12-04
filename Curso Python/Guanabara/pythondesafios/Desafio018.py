#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import sin,cos,tan,radians
num = float(input('Digite um angulo: '))
seno = sin(radians(num))
print('O ângulo de {}° em SENO é {:.2f}.'.format(num,seno))
cosseno = cos(radians(num))
print('O ângulo de {}° em COSSENO é {:.2f}.'.format(num,cosseno))
tang = tan(radians(num))
print('O ângulo de {}° na TANGENTE é {:.2f}'.format(num,tang))
