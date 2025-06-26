#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milímetros.(adicionando todas as medidas)
n = float(input('Digite um numero em metros para descobrir quanto ele vale em centimetros e milímetros:'))
dm = n * 10
cm = n * 100
mm = n * 1000
dam = n / 10
hm = n / 100
km = n / 1000

print('{} metros em todas as medidas são: \nEm decimetro é igual a {} \nEm centimetros é igual a {}.\nEm milímetros é igual a {}\nEm decâmetro é igual a {}\nEm hectômetro é igual a {}\nEm quilômetro é igual a {} '.format(n,dm, cm, mm,dam,hm,km))