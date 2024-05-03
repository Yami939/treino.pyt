import pygame
from pygame.locals import *
from sys import exit
from random import randint
pygame.init()

largura = 640
altura = 480 
x = largura/2
y = altura/2
relogio = pygame.time.Clock()

x_verde = randint(40,600)
y_verde = randint(50,430)

tela = pygame.display.set_mode((largura, altura))

pygame.display.set_caption('CrazyRacing: Less Wanted')

while True: 
    
    relogio.tick(10)
    tela.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        
        # if event.type == KEYDOWN:
        #      if event.key == K_a:
        #          x = x - 20
        #      if event.key == K_d:
        #          x = x + 20
        #      if event.key == K_w:
        #          y = y - 20
        #      if event.key == K_s:
        #          y = y + 20 
                         
        if pygame.key.get_pressed()[K_a]:
            x = x - 20
        if pygame.key.get_pressed()[K_d]:
            x = x + 20    
        if pygame.key.get_pressed()[K_w]:
            y = y - 20
        if pygame.key.get_pressed()[K_s]:
            y = y + 20          
       
    ret_roxo = pygame.draw.rect(tela, (60,26,198), (x,y,40,50))
    ret_verde = pygame.draw.rect(tela, (17,179,187), (x_verde,y_verde,40,50))
     
    if ret_roxo.colliderect(ret_verde):
        x_verde = randint(40,600)
        y_verde = randint(50,430)
    pygame.display.update()
