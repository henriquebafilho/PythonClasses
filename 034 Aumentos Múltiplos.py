'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%. Para inferiores ou iguais, o aumento é de 15%.'''
print('Calcule o valor do seu aumento!')
print('Salários maiores que R$1250,00 têm aumento de 10%.')
print('Salários menores ou iguais a R$1250,00 têm aumento de 15%.')
salario = float(input('Insira seu salário atual: R$'))
aumento = 0
novo_salario = 0

if salario > 1250.00:
    aumento = salario * (10 / 100)
else:
    aumento = salario * (15 / 100)

novo_salario = salario + aumento
print('Seu salário era de R${:.2f} e sofreu um aumento de {:.2f}'.format(salario, aumento))
print('Portanto, seu novo salário é R${:.2f}'.format(novo_salario))
