#Faça um programa que leia a largura e a altura de uma parede em metros,
#Calcule a sua área e a quantidade de tinta necessária para pintá-la,
#Sabendo que cada litro de tinta pinta uma área de 2m²
largura = float(input('Insira a largura da parede: '))
altura = float(input('Insira a altura da parede: '))
area = largura * altura
tintaTotal = area / 2

print('A área da parede é ', area, 'm²')
print('É necessário ', tintaTotal, 'litros de tinta para pintar a parede')