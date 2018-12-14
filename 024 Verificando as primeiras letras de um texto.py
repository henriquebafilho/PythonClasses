'''Crie um programa que leia o nome de uma cidade e e diga se ela começa ou não com o nome "Santo".'''
cidade = input('Insira o nome da cidade: ')

if cidade.split()[0] == 'Santo' or cidade.split()[0] == 'santo':
    print('A cidade', cidade, 'começa com "Santo".')
else:
    print('A cidade', cidade, 'não começa com "Santo".')