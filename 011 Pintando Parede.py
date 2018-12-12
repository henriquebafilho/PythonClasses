#
largura = float(input('Insira a largura da parede: '))
altura = float(input('Insira a altura da parede: '))
area = largura * altura
tintaTotal = area / 2

print('A área da parede é ', area, 'm²')
print('É necessário ', tintaTotal, 'litros de tinta para pintar a parede')