# import pygame
# import sys


# pygame.init()

#   # APLICAR UM 
#         # RETANGULO ** 
#         # ELIPSE ** 
#         # DOCUMENTAÇÃO 
#         # PESQUISA    


# WIDTH = 800
# LENGTH = 600




# tela = pygame.display.set_mode((WIDTH,LENGTH ))
# pygame.display.set_caption('RETANGULO')


# #loop da página 
# run = True

# while run:
#     for evento in pygame.event.get():
#         if evento.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit

#         cor = (240,230,140)
#         tela.fill(cor)
#         pygame.draw.rect(tela, ("red"), (100,100,200,150), 50)
#         pygame.draw.ellipse(tela,('black'), (100,100,200,150), 20)

#         pygame.display.flip()




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


