'''Faça um programa que leia uma frase pelo teclado e mostre:
-Quantas vezes aparece a letra "A"
-Em que posição ela aparece a primeira vez
-Em que posição ela aparece a última'''
frase = input('Insira uma frase: ')
qtdA = frase.count('A')

print('A letra A aparece {} vezes.'.format(qtdA))