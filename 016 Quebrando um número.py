'''Crie um programa que leia um número qualquer pelo teclado
e mostre na tela sua porção inteira.
Ex.: Digite um número: 6.127
O número 6.127 tem a parte inteira 6'''
from math import trunc
numero = float(input('Digite um número qualquer: '))
inteiro = trunc(numero) #trunc corta a parte inteira do número

print('A parte inteira de {} é {}'.format(numero, inteiro))
print('A parte inteira de {} é {}'.format(numero, int(numero))) #transforma o número em int