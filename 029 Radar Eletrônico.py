'''Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.'''
velocidade = int(input('Insira a velocidade atual do carro em km/h: '))

if velocidade > 80:
    multa = (velocidade - 80) * 7.00
    print('Atenção!! Você foi multado por excesso de velocidade!!!')
    print('Você está a {}km/h e o permitido é até 80km/h.'.format(velocidade))
    print('Você terá que pagar uma multa de R${:.2f}.'.format(multa))
else:
    print('Parabéns! Você está na velocidade permitida.')
