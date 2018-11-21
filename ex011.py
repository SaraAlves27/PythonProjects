l = float(input('Qual é a largura da parede a ser pintada(m)? '))
alt = float(input('E a sua altura(m)? '))
a = l * alt
t = a / 2
print('Sua parede tem a dimensão de {}X{} e sua área é de {}m².'.format(l,alt,a))
print('Voce vai precisar de {:.1f} litros de tinta para pinta-la.'.format(t))

