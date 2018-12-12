# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais
# ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado.
kilometros = float(input('Quantos kilômetros você rodou com o carro? '))
dias = int(input('Por quantos dias ele foi alugado? '))
total = (60 * dias) + (0.15 * kilometros)

print('O preço total é R${:.2f}'.format(total))