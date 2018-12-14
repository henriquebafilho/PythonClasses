'''Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida
o primeiro e o último nome separadamente.
Ex.: Ana Maria de Souza
Primeiro = Ana
Último = Souza'''
nomeCompleto = input('Insira o nome completo da pessoa: ')
nomeCompleto = nomeCompleto.split()
primeiro = nomeCompleto[0]
ultimo = nomeCompleto[len(nomeCompleto)-1]

print('O primeiro nome da pessoa é {}'.format(primeiro))
print('O último nome da pessoa é {}'.format(ultimo))