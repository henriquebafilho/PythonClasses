'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se
alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também
 deverá mostrar o tempo que falta ou que passou do prazo.'''
from datetime import date
anoNascimento = int(input('Insira o ano que você nasceu: '))
idade = date.today().year - anoNascimento
anoAlistamento = anoNascimento + 18
tempo = 0

print("Seu ano de alistamento é {}".format(anoAlistamento))
print("Você tem {} anos".format(idade))
if idade < 18:
    tempo = 18 - idade
    print("Ainda faltam {} anos para você se alistar.".format(tempo))
elif idade == 18:
    print("Você tem 18 anos. É a hora exata de você se alistar.")
else:
    tempo = idade - 18
    if tempo == 1:
        print("Já passou 1 ano da época que você deveria se alistar.")
    else:
        print("Já passaram {} anos da época que você deveria se alistar.".format(tempo))