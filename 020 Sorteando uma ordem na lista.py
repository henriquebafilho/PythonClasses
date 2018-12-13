'''O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
 Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.'''
import random

alunos = ["Allan", "JV", "Peru", "Rickão"]
ordem = random.shuffle(alunos) #embaralhar lista

print(alunos)