'''Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.'''
import random

print('Vou pensar um número entre 0 e 5. Tente adivinhar...')
n1 = random.randint(0, 5)
n2 = int(input('Insira um número entre 0 e 5: '))

print('Eu pensei no número {} e você no número {}'.format(n1,n2))
if n1 == n2:
    print('Parabéns!! Você adivinhou!')
else:
    print('Errrrrooouuuuu')
