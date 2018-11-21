s = float(input('Qual é o valor do  salário atual do funcionário? '))
if s > 1250:
    sn = s * 10 / 100
else:
    sn = s * 15 / 100
print('Esse funcionário receberá um aumento de R${:.2f}.Portanto seu novo salário será de R${:.2f}'.format(sn ,s + sn))



