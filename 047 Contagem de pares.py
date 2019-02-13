'''Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.'''
contador = 1
evens = []
while contador <= 50:
    if(contador%2==0):
        evens.append(contador)
    contador += 1
print(evens)
print("quantidade:", len(evens))