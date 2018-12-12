#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
valor = float(input('Insira o valor em metros: '))
centimetros = valor * 100
milimetros = valor * 1000

print(valor, 'm = ', centimetros, 'cm')
print(valor, 'm = ', milimetros, 'mm')