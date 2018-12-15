'''Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não
formar um triângulo.'''
print('Cheque se os valores inseridos podem formar um triângulo!')
n1 = int(input('Insira o primeiro valor: '))
n2 = int(input('Insira o segundo valor: '))
n3 = int(input('Insira o terceiro valor: '))

if n1 < n2 + n3 and n1 > abs(n2 - n3):
    print('Pode-se criar um triângulo com os valores {}, {} e {}.'.format(n1, n2, n3))
else:
    print('Não se pode criar um triângulo com os valores {}, {} e {}.'.format(n1, n2, n3))
