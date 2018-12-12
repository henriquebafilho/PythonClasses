#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabual
numero = int(input('Digite um número inteiro: '))
contador = 1

while contador <= 10:
    print(numero, ' x ', contador, ' = ', (numero * contador))
    contador = contador + 1