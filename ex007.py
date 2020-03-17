# ler 2 notas, calcular e mostrar a média.

print('            média entre 2 números')
nome = input('Nome do aluno: \n')
n1 = float(input('Digite sua primeira nota: \n'))
n2 = float(input('Digite sua segunda nota: \n'))
media = (n1 + n2) / 2
print('a média de {} é: {:.1f}'.format(nome, media))