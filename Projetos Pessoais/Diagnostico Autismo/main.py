print('Tabela')
n = list(range(1, 11))
sim = []
nao = []

# Coleta de dados
for lista in n:
    valor = input(f'Seu filho faz o {lista}? s/n ')
    if valor.lower() == 's':
        sim.append(lista)
    else:
        nao.append(lista)

print(f'\nSeu filho faz as atividades {sim}')
print(f'Seu filho não faz as atividades {nao}')

grupo_atual = []
todos_grupos = []

for numero in n:
    if numero in sim:
        grupo_atual.append(numero)
    else:  # numero está em nao
        if grupo_atual:
            print(f"Seu filho não fez a atividade {numero}, então reveja: {grupo_atual}")
            todos_grupos.append(grupo_atual)
            grupo_atual = []  # reinicia o grupo

if grupo_atual:
    todos_grupos.append(grupo_atual)

print(f'\nGrupos de atividades consecutivas feitas:')
for grupo in todos_grupos:
    print(grupo)
