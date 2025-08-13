import pygame


pygame.init()

tela = pygame.display.set_mode((500,500))

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        tela.fill('blue')
        pygame.draw.rect(tela, (255,0,0),(220,220,50,50))
        pygame.display.flip()


