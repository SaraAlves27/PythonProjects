dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
pdias = dias * 60
pkm = km * 0.15
total = pdias + pkm
print('O total a pagar é de  R${:.2f}'.format(total))