#Quanto tem na carteira e quantos dolares da para comprar(US$ 1 = R$3.27) 

reais = float(input('Quantos reais você tem? ')) 
dol = reais / 3.27
print('Você pode comprar US${:.2f} '.format(dol))
