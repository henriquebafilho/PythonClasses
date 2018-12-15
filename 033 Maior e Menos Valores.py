'''Faça um programa que leia três números e mostre qual é o maior e qual é o menor.'''
maior = 0
menor = 0
print('Veja qual número é maior!')
n1 = int(input('Insira o primeiro número: '))
n2 = int(input('Insira o segundo número: '))
n3 = int(input('Insira o terceiro número: '))

if n1 >= n2:
    if n1 > n3:
        maior = n1
        if n2 <= n3:
            menor = n2
        else:
            menor = n3
    else:
        maior = n3
        if n2 <= n1:
            menor = n2
        else:
            menor = n1
else:
    if n2 >= n3:
        maior = n2
        if n1 <= n3:
            menor = n1
        else:
            menor = n3
    else:
        maior = n3
        menor = n1

print('O maior número é {}'.format(maior))
print('O menor número é {}'.format(menor))