#Um algoritmo que leia um preço de um produto e mostre seu novo preço com 5% de desconto

preço = float(input('Digite o preço para ganhar desconto: '))
valordesco = preço * 0.05
preçofinal= preço * 0.95
print('Valor do desconto: {:.2f}'.format(valordesco))
print('Valor a ser pago {:.2f}'.format(preçofinal))
