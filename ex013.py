salario = float(input('Digite o salário do funcionario:R$  ' ))
aumento = salario * 15 /100
novo = salario + aumento
print('O  funcionario que tinha o salario de R${:.2f} com 15% de aumento terá R${:.2f} '.format(salario,novo))