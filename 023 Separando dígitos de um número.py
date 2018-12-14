'''Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
Ex.: Digite um número: 1834
Unidade: 4
Dezena: 3
Centena: 8
Milhar: 1'''

numero = input('Insira um número inteiro de 0 a 9999: ')
unidade = numero[len(numero)-1]
dezena = numero[len(numero)-2]
centena = numero[len(numero)-3]
milhar = numero[len(numero)-4]

print('Unidade:', unidade)
print('Dezena:', dezena)
print('Centena:', centena)
print('Milhar:', milhar)