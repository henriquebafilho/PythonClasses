#Faça um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
#Considere US$=1.00 = R$3.27
real = float(input('Insira umaa quantidade de dinheiro em real: R$'))
dolar = real/3.27

print('R${:.2f} = US${:.2f}'.format(real, dolar))