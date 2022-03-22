'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
-Se ele ainda vai se alistar ao serviço militar.
-Se é a hora de se alistar.
-Se já passou o tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''
from datetime import date
print('Vamos descobrir quando você precisa se alistar no exercito')
m = int(input('''Você é homem ou mulher?
[1] para Mulher
[2] para Homem
Resposta: '''))
if m == 1:
    print('Você não precisa fazer o alistamento obrigatório')
else:
    atual = date.today().year
    nasceu = int(input('Em que ano você nasceu?:'))
    idade = atual - nasceu

    if idade < 18:
        print(f'Quem nasceu em {nasceu}, tem {idade} anos de idade em {atual}.')
        print('Ainda faltam {} anos para o alistamento'.format(18 - idade))
        print('Seu alistamento será em {}.'.format((18-idade) + atual))
    elif idade > 18:
        print(f'Quem nasceu em {nasceu}, tem {idade} anos de idade em {atual}.')
        print('Você ja deveria ter se alistado há {} anos'.format(idade - 18))
        print('Seu alistamento foi em {}.'.format(atual - (idade - 18)))
    else:
        print(f'Quem nasceu em {nasceu}, tem {idade} anos de idade em {atual}.')
        print('Você tem que se alistar IMEDIATAMENTE!')