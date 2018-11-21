from math import sin,radians,cos,tan
a = float(input('Digite o angulo que voce deseja: '))
seno = sin(radians(a))
print('O seno de {:.0f} é {:.2f}'.format(a,seno))
cosseno = cos(radians(a))
print('O cosseno de {:.0f} é {:.2f}'.format(a,cosseno))
tangente = tan(radians(a))
print('A tangente de {:.0f} é {:.2f}'.format(a,tangente))