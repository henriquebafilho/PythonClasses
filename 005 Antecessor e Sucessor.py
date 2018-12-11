#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor
numero = int(input('Insira um número: '))
antecessor = numero - 1
sucessor = numero + 1
print('O antecessor de {} é {}'.format(numero, antecessor))
print('O sucessor de {} é {}'.format(numero, sucessor))
print('O antecessor de {} é {}'.format(numero, numero-1))