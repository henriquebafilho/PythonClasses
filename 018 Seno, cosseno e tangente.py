#Faça um programa que leia um ângulo qualquer e mostre na tela o valor
# do seno, cosseno e tangente desse ângulo.
import math
angulo = float(input('Insira o valor do ângulo em radianos: '))
seno = math.sin(angulo)
cosseno = math.cos(angulo)
tangente = math.tan(angulo)

print('seno = {}'.format(seno))
print('cosseno = {}'.format(cosseno))
print('tangente = {}'.format(tangente))