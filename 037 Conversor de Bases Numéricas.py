'''Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de
conversão: 1 para binário, 2 para octal e 3 para hexadecimal.'''
numero = int(input('Insira o número a ser convertido: '))
base = int(input('''Insira a base numérica que o número {} será convertido:
    1 - binário
    2 - octal
    3 - hexadecimal
    '''.format(numero)))

while base < 1 or base > 3:
    base = int(input('''Erro! Escolha um número de 1 a 3:
        1 - binário
        2 - octal
        3 - hexadecimal
        '''))

if(base == 1):
    print('{} em binário é {}'.format(numero, bin(numero)[2:]))
elif(base == 2):
    print('{} em octal é {}'.format(numero, oct(numero)[2:]))
elif(base == 3):
    print('{} em hexadecimal é {}'.format(numero, hex(numero)[2:]))