#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada
numero = int(input('Digite um número: '))
dobro = numero * 2
triplo = numero * 3
potencia = pow(numero, 2)
raiz = numero ** (1/2)
print('O dobro de {} é {}'.format(numero, dobro))
print('O triplo de {} é {}'.format(numero, triplo))
print('A raiz quadrada de {} é {}'.format(numero, raiz))
print('{} ao quadrado é {}'.format(numero, potencia))
print('O dobro de {} é {} \nO triplo de {} é {} \nE a raiz quadrada de {} é {:.2f}'.format(numero, dobro, numero, triplo, numero, raiz))