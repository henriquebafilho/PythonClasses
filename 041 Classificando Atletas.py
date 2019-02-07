'''A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER'''
from datetime import date
nascimento = int(input("Insira o ano de nascimento do atleta: "))
idade = date.today().year - nascimento

print("Sua idade é {}".format(idade))
if idade <= 9:
    categoria = "MIRIM"
elif idade > 9 and idade <= 14:
    categoria = "INFANTIL"
elif idade > 14 and idade <= 19:
    categoria = "JÚNIOR"
elif idade > 19 and idade <= 25:
    categoria = "SÊNIOR"
else:
    categoria = "MASTER"

print("Sua categoria é {}".format(categoria))