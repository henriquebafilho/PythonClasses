#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
dolar = 3.9
real = float(input('Insira umaa quantidade de dinheiro em real: '))
total = real/dolar

print('R$', real, ' = US$', total)