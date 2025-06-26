#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessário para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m**2.
n = float(input('Digite a largura de sua parede em metros:'))
n2 = float(input('Digite a altura de sua parede em metros:'))
a = n * n2
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m2.'.format(n,n2,a))
t = a / 2
print('Para pintar essa parede, você precisará de {}l de tinta'.format(t))

