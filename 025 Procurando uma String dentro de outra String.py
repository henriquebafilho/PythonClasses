'''Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.'''
nomeCompleto = input('Insira o nome completo da pessoa: ').strip()
nomeCompleto = nomeCompleto.split()
temSilva = False

for nome in nomeCompleto:
    if nome.capitalize() == 'Silva':
        temSilva = True

if temSilva == True:
    print('A pessoa tem Silva no nome.')
else:
    print('A pessoa não tem Silva no nome.')