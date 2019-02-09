'''Crie um programa que faça o computador jogar Jokenpô com você.'''
import random
usuário = int(input('''Insira o número que corresponde à sua escolha:
1 - pedra
2 - papel
3 - tesoura
'''))
while usuário < 1 or usuário > 3:
    usuário = int(input("Erro! Insira um valor válido: "))

def objeto(numero):
    if numero == 1:
        return "pedra"
    elif numero == 2:
        return "papel"
    else:
        return "tesoura"

computador = random.randint(1, 3)

def checagem(user, pc):
    if (user == 1 and pc == 2) or (user == 2 and pc == 3) or (user == 3 and pc == 1):
        return "Você perdeu"
    elif (user == 1 and pc == 3) or (user == 2 and pc == 1) or (user == 3 and pc == 2):
        return "Você ganhou!"
    else:
        return "Empate"

print("A minha escolha foi {}".format(objeto(computador)))
print(checagem(usuário, computador))
