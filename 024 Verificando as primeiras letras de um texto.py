'''Crie um programa que leia o nome de uma cidade e e diga se ela começa ou não com o nome "Santo".'''
cidade = input('Insira o nome da cidade: ').strip()
primeiroNome = cidade.split()[0].capitalize()

if primeiroNome == 'Santo':
    print('A cidade', cidade, 'começa com "Santo".')
else:
    print('A cidade', cidade, 'não começa com "Santo".')