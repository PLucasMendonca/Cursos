#Faça um algoritimo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input('Digite o valor de seu salário: '))
novo_salario = salario +(salario * 15/100)
print('Seu salario de {:.2f} R$ com 15% de aumento fica {:.2f} R$'.format(salario, novo_salario))