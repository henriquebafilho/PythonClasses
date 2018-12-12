#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto
preco = float(input('Insira o preço do produto: R$'))
total = preco - (preco * (5/100))

print('O novo preço é R$', total)