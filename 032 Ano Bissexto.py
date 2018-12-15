'''Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.'''
ano = int(input('Insira um ano para ver se ele é bissexto: '))
bissexto = False

if ano % 4 == 0:
    if ano % 100 != 0:
        bissexto = True
else:
    if ano % 400 == 0:
        bissexto = True

if bissexto:
    print('O ano {} é bissexto.'.format(ano))
else:
    print('O ano {} não é bissexto.'.format(ano))