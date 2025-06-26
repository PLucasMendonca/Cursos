'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A)Quantas vezes apareceu o valor 9.
B)Em que posição foi digitado o primeiro valor 3.
C)Quais foram os número pares.'''

n = (int(input('Digite um número: ')),int(input('Digite outro número: ')),int(input('Digite mais um número: ')),int(input('Digite o ultimo número: ')))
print(f'Você digitou {n}')
print(f'O número 9 apareceu {n.count(9)} vezes')
if 3 in n:
    print(f'O número 3 apareceu na posição de número {n.index(3)+1}')
else:
    print('O número 3 não foi digitado')

print(f'Os números pares digitados foram :', end='')
for numero in n:
    if numero % 2 == 0:
        print(numero, end='')