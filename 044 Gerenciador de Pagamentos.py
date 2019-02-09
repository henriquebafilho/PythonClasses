'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros'''
preçoNormal = float(input("Insira o preço normal do produto: "))
pagamento = int(input('''Insira o número correspondente à forma de pagamento: 
                        1 - à vista dinheiro/cheque: 10% de desconto 
                        2 - à vista no cartão: 5% de desconto 
                        3 - em até 2x no cartão: preço formal 
                        4 - 3x ou mais no cartão: 20% de juros
                        '''))
while pagamento < 1 or pagamento > 4:
    pagamento = int(input('''Erro! Insira um valor válido: '''))

if pagamento == 1:
    preçoFinal = preçoNormal - (preçoNormal * 10 / 100)
    tipo = "à vista dinheiro/cheque"
elif pagamento == 2:
    preçoFinal = preçoNormal - (preçoNormal * 5 / 100)
    tipo = "à vista no cartão"
elif pagamento == 3:
    preçoFinal = preçoNormal
    tipo = "em até 2x no cartão"
else:
    preçoFinal = preçoNormal + (preçoNormal * 20 / 100)
    tipo = "3x ou mais no cartão"

print('''Tipo de pagamento selecionado: {}
        Preço final: R${}'''.format(tipo, preçoFinal))




