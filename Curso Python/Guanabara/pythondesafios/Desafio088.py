'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.'''

from time import sleep
from random import randint
print('-'*30)
print('     JOGA NA MEGA SENA     ')
print('-'*30)
lista = []
jogos = list()
s = int(input('Quantos jogos você quer sortear ? '))
tot = 1
while tot <= s:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >=6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f'SORTEANDO {s} JOGOS', '-=' * 3)
for i, l in enumerate (jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-='*5, '< BOA SORTE >', '-=' * 5)

