'''Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar.'''
numero = int(input('Insira um número: '))

if numero % 2 == 0:
    print('{} é par.'.format(numero))
else:
    print('{} é ímpar.'.format(numero))

#if simplificado
print('{} é par.'.format(numero) if numero % 2 == 0 else '{} é ímpar.'.format(numero))