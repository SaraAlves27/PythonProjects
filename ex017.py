'''from math import hypot
co = float(input('Digite o comprimento do cateto oposto : '))
ca = float(input('Digite o comprimento do cateto adjacente : '))
print('A hipotenusa vai medir : {:.2f} '.format(hypot(co,ca)))'''

co = float(input('Digite o comprimento do cateto oposto : '))
ca = float(input('Digite o comprimento do cateto adjacente : '))
h = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir : {:.2f}'.format(h))
