import pygame
import sys


pygame.init()


WIDTH = 500
LENGTH = 400




tela = pygame.display.set_mode((WIDTH, LENGTH))
pygame.display.set_caption('Teste')


#loop da página 
run = True

while run:
    for event in pygame.event.get():


        if event.type == pygame.QUIT:
          run = False
          pygame.quit()
          sys.exit() 
        
        cor =  (240,230,140)
        tela.fill(cor)       
        pygame.draw.circle(tela, ('red'), (250,200), 50)
        pygame.draw.circle(tela, ('black'), (10,20), 20)


        # APLICAR UM 
        # RETANGULO ** 
        # ELIPSE ** 
        # DOCUMENTAÇÃO 
        # PESQUISA       


        pygame.display.flip()



      # APLICAR UM 
        # RETANGULO ** 
        # ELIPSE ** 
        # DOCUMENTAÇÃO 
        # PESQUISA   

import pygame
import sys

pygame.init()

width = 700
height = 500

screen = pygame.display.set_mode((width, height)) 

quandrado =  pygame.Rect(350,200, 150,70)
rectangulo2 = pygame.Rect(10,150, 50,50)

clock =  pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           pygame.quit() 
           sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                quandrado.move_ip([10,0])
            if event.key == pygame.K_LEFT:
                quandrado.move_ip([-10,0])
            if event.key == pygame.K_UP:
                quandrado.move_ip([0,-10])
            if event.key == pygame.K_DOWN:
                quandrado.move_ip([0,10])     

        
        screen.fill('red')
        pygame.draw.rect(screen,('green'), quandrado)
        pygame.draw.rect(screen,('white'), rectangulo2)
        pygame.display.update()