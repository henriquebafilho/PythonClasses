'''Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da
passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.'''
print('=' * 20)
print('Viagens de até 200km = R$0,50 por km')
print('Viagens de mais de 200km = R$0,45 por km')
print('=' * 20)
kilometros = int(input('Insira quantos km tem sua viagem: '))
preco = 0

if kilometros <= 200:
    preco = kilometros * 0.5
else:
    preco = kilometros * 0.45
    
print('O preço da sua viagem é R${:.2f}.'.format(preco))
