'''Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes'''
print('Cheque se os valores inseridos podem formar um triângulo!')
n1 = int(input('Insira o primeiro valor: '))
n2 = int(input('Insira o segundo valor: '))
n3 = int(input('Insira o terceiro valor: '))

if n1 < n2 + n3 and n1 > abs(n2 - n3):
    if n1 == n2 and n2 == n3:
        tipo = "equilátero"
    elif n1 == n2 or n2 == n3 or n1 == n3:
        tipo = "isósceles"
    else:
        tipo = "escaleno"
    print('Pode-se criar um triângulo {} com os valores {}, {} e {}.'.format(tipo, n1, n2, n3))
else:
    print('Não se pode criar um triângulo com os valores {}, {} e {}.'.format(n1, n2, n3))