#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
salario = float(input('Insira seu salário: R$'))
total = salario + (salario * (15/100))

print('Seu novo salário é R${:.2f}'.format(total))