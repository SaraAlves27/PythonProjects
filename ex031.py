d = float(input('Qual é a distancia da sua viagem? '))
print('Voce esta prestes a começar uma viagem de {:.1f}Km. '.format(d))
if d > 200:
    c = d * 0.45
else:
    c = d * 0.50
print('E o preço da sua viagem será de R${:.2f}'.format(c))

#EXERCICIO RESOLVIDO COM O IF SIMPLIFICADO:

d = float(input('Qual é a distancia da sua viagem? '))
print('Voce esta prestes a começar uma viagem de {:.1f}Km.'.format(d))
preco = distancia * 0.50 if d <= 200 else distancia * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preco))



