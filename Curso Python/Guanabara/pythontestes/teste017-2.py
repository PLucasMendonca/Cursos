galera = list()
dado = list()
totmai = totmen = 0
for c in range(0,3):
  dado.append(str(input('Nome: ')))
  dado.append(int(input('Idade: ')))
  galera.append(dado[:])
  dado.clear()
for p in galera:
  if p[1] >=21:
    print(f'{p[0]} é maior de idade.')
    totmai +=1
  else:
    print(f'{p[0]} é menor de idade.')
    totmen +=1
print(f'Temos {totmai} maiores e {totmen} menores de idade')





'''galera = list()
dado = list()
for c in range(0,3):
  dado.append(str(input('Nome: ')))
  dado.append(int(input('Idade: ')))
  galera.append(dado[:])
  dado.clear()
print(galera)

galera = [['Lucas', 21], ['Tai', 20], ['Gui', 23], ['Geo',25]]
for p in galera:
  print(f'{p[0]} tem {p[1]} anos de idade.')

for p in galera:
  print(p[0]) so os nomes

for p in galera:
  print(p)'''