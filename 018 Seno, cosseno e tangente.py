#Faça um programa que leia um ângulo qualquer e mostre na tela o valor
# do seno, cosseno e tangente desse ângulo.
import math
angulo = float(input('Insira o valor do ângulo em radianos: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('seno = {:.2f}'.format(seno))
print('cosseno = {:.2f}'.format(cosseno))
print('tangente = {:.2f}'.format(tangente))