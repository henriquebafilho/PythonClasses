#Faça um programa que lia um número inteiro qualquer e mostre na tela a sua tabuada
numero = int(input('Digite um número inteiro: '))
contador = 1

print('='*20)
while contador <= 10:
    print('{} x {:2} = {}'.format(numero, contador, numero*contador))
    contador = contador + 1
print('='*20)