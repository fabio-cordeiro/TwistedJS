#Um algoritmo que leia o salario de um funcionario e mostre com 15% de aumento.

salario = float(input(' Qual o valor do sálario? '))
aumento = salario * 0.15
nsalario = salario + aumento
print('O valor do aumento é: {:;2f}'.format(aumento))
print('Sálario com reajuste: {:.2f}'.format(nsalario))
