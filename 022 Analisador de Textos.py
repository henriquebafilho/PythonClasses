'''Crie um programa que leia o nome completo de uma pessoa e mostre:
-O nome com todas as letras maiúsculas
-O nome com todas minúsculas
-Quantas letras ao todo (sem considerar espaços)
-Quantas letras tem o primeiro nome'''

nome = input('Insira o nome completo da pessoa: ').strip()
maiusculo = nome.upper()
minusculo = nome.lower()
qtdSemEspaco = len(nome) - nome.count(' ')
primeiroNome = nome.split()[0]
qtdPrimeiroNome = len(primeiroNome)

print(maiusculo)
print(minusculo)
print(nome, 'tem', qtdSemEspaco, 'letras sem espaço')
print(primeiroNome, 'tem', qtdPrimeiroNome, 'letras.')