from random import randint
from time import sleep
print('Estou pensando.....')
sleep(3) #Faz o compultador dormir por 3 segundos
compultador = randint(0,5) #Faz o compultador "pensar"
print('-=-' * 20)
print('Pensei em um número inteiro entre 0 e 5.')
print('Voce consegue descobrir que número é esse? ')
print('-=-' * 20)
jogador = int(input('Digite o número em que voce acha que eu pensei: ')) #Jogador tenta adivinhar
print('-=-' * 20)
if compultador == jogador:
    print('PARABENS!! VOCE CONSEGUIU ME VENCER')
else:
    print('DESCULPE, VOCE PERDEU')
    print('O número que eu havia pensado era {}'.format(compultador))
print('-=-' * 20)




