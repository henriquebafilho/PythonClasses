# Escreva um programa que converta uma temperatura digitada em ºC para ºF.
celsius = float(input('Digita a temperatura: ºC'))
fahrenheit = ((9 * celsius) / 5) + 32

print('{}ºC = {}ºF'.format(celsius, fahrenheit))
