#ler um valor em metros e exibir convertidos em centimetros e milimetros

m = float(input('Quantos metros? '))
cm = m * 100
mm = m * 1000
print('{} metros tem {} centimetros e {} milimetros'.format(m, cm, mm))
