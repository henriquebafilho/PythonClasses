#Faça um programa em Python que abra e reproduza o áudio de um arquivo mp3

'''Não funciona
import pygame
pygame.init()
pygame.mixer.music.load('021.mp3')
pygame.mixer.music.play()
pygame.event.wait()'''

'''funciona'''
import playsound
playsound.playsound('021.mp3')