'''Faça um programa que leia uma frase pelo teclado e mostre:
-Quantas vezes aparece a letra "A"
-Em que posição ela aparece a primeira vez
-Em que posição ela aparece a última'''
frase = input('Insira uma frase: ').lower().strip()
qtdA = frase.count('a')

print('A letra A aparece {} vezes.'.format(qtdA))
print('A primeira letra A aparece na posição {}'.format(frase.find('a')+1))
print('A última letra A aparece na posição {}'.format(frase.rfind('a')+1))