'''Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais'''
primeiro = int(input('Insira o primeiro número: '))
segundo = int(input('Insira o segundo número: '))

if primeiro > segundo:
    print('O primeiro ({}) é maior que o segundo ({})'.format(primeiro, segundo))
elif segundo > primeiro:
    print('O segundo ({}) é maior que o primeiro ({})'.format(segundo, primeiro))
else:
    print('O primeiro ({}) e o segundo ({}) são iguais'.format(primeiro, segundo))