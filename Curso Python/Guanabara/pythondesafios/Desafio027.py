'''Faça um programa que leia o nome completo de uma pessoa,mostrando em seguida o primeiro e o último nome separadamente.
Ex:Ana Maria de Souza
primeiro = Ana
último = Souza.'''
nome = str(input('Digite seu nome completo: ')).strip()
separado = nome.split()
print('Seu primeiro nomé é: {}'.format(separado[0]))
print('Seu ultimo nome é: {}'.format(separado[len(separado)-1]))
