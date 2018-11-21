preço = float(input('Digite o preço do produto: R$ '))
desconto = int(input('Digite a porcentagem de desconto: '))
porcentagem = (preço * desconto) / 100
print('Com o desconto de {}% o valor a ser descontado será  de R${:.2f} '.format(desconto,porcentagem))
novo = preço - porcentagem
print('O novo preço será R${:.2f} reais'.format(novo))