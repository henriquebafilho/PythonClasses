'''Faça um programa que leia o comprimento do cateto oposto e do cateto
 adjacente de um triângulo retângulo, calcule e mostre o comprimento
 da hipotenusa.'''
import math

oposto = float(input('Digite o cateto oposto: '))
adjacente = float(input('Digite o cateto adjacente: '))
hipotenusa = math.hypot(oposto, adjacente)
# hipotenusa = sqrt(pow(oposto, 2) + pow(adjacente,2))

print('A hipotenusa é {:.2f}'.format(hipotenusa))
