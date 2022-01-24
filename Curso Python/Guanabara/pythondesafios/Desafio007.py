#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média.
n = float(input('Digite sua nota:'))
n2 = float(input('Digite sua outra nota:'))
m = (n + n2) / 2
print('A média da sua nota foi = {:.1f}'.format(m))
