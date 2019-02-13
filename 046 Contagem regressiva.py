'''Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0,
com uma pausa de 1 segundo entre eles.'''
import time
from datetime import date
tempo = 10

print(tempo)
while tempo > 0:
    time.sleep(1)
    tempo -= 1
    print(tempo)
print("FELIZ ANO {}".format(date.today().year))