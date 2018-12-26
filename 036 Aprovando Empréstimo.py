'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
 Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
 A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''

print('Empréstimos de casas do Rickão')
valor = float(input('Insira o valor da casa que deseja adquirir: R$'))
salario = float(input('Insira o valor do seu salário: R$'))
anos = float(input('Em quantos anos você vai pagar a casa? '))
prestacao = valor / (anos * 12)
trintaPorCento = salario * 30 / 100

if (prestacao > trintaPorCento):
    print('O negócio não pode ser fechado pois o valor da prestação é maior que 30% do seu salário.')
else:
    print('Empréstimo aprovado com sucesso!')

print('Prestação por mês: R${:.2f}'.format(prestacao))
print('30% do seu salário: R${:.2f}'.format(trintaPorCento))
