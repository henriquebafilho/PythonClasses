'''Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.'''
contador = 0
múltiplos = []
soma = 0
#colocando múltiplos de 3 em um array
while contador <= 500:
    if contador % 3 == 0:
        múltiplos.append(contador)
    contador += 1
#somando todos os múltiplos de 3
for x in múltiplos:
    soma += x
#mostrando soma
print(soma)