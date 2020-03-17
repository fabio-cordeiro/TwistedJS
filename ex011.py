# leia a largura e a altura de uma parece em metros. calcule sua área quadrada e a quantidade
# de tinta para pintá-la. sabendo que cada litro de tinta pinta 2m^2.]

a = float(input('a parede tem quantos metros de altura? '))
l = float(input('e quantos metros de largura? '))
m2 = l * a
t = m2 / 2
print('a parede tem {} metros quadrados'.format(m2))
print('É nescessario {} litros de tinta'.format(t))

