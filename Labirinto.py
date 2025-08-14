# MANIPULAÇÃO DOS EVENTOS
# JOGO LABIRINTO

import pygame

# Inicializa o Pygame
pygame.init()



# COMENTE O CÓDIGO, EXPLIQUE COM SUAS PALAVRAS O QUE ESTA OCORRENDO EM CADA ESTRUTURA DO 
# CÓDIGO E VERIFIQUE O QUE OCORRE. 
# CONSULTE A BIBLIOTECA -> https://www.pygame.org/docs/




#estrura para tela utilizado variaveis chamano os modoluos do pygame
largura, altura = 400, 400
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Labirinto")

#cores para o labirinto 
preto = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (255, 0, 0)

#utilização de lista para estrutura do labirinto 
tamanho_celula = 40
labirinto = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 0, 0, 1, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


x, y = 1 * tamanho_celula, 1 * tamanho_celula
velocidade = 40

#função para desenhar o labirinto
def desenhar_labirinto():
    for linha in range(len(labirinto)):
        for coluna in range(len(labirinto[linha])):
            cor = preto if labirinto[linha][coluna] == 1 else branco
            pygame.draw.rect(tela, cor, (coluna * tamanho_celula, linha * tamanho_celula, tamanho_celula, tamanho_celula))

#loop principal do jogo
executando = True
while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False


#movimentação dos joadores condicionado em 
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        novo_x = x - velocidade
        if labirinto[y // tamanho_celula][novo_x // tamanho_celula] == 0:
            x = novo_x
    if teclas[pygame.K_RIGHT]:
        novo_x = x + velocidade
        if labirinto[y // tamanho_celula][novo_x // tamanho_celula] == 0:
            x = novo_x
    if teclas[pygame.K_UP]:
        novo_y = y - velocidade
        if labirinto[novo_y // tamanho_celula][x // tamanho_celula] == 0:
            y = novo_y
    if teclas[pygame.K_DOWN]:
        novo_y = y + velocidade
        if labirinto[novo_y // tamanho_celula][x // tamanho_celula] == 0:
            y = novo_y


    tela.fill(branco)

    #desenho do labirinto chamado a função 
    desenhar_labirinto()
    pygame.draw.rect(tela, vermelho, (x, y, tamanho_celula, tamanho_celula))

    #Atualização da Tela
    pygame.display.flip()

    #Controle do tempo onde define a velocidade da atualização do jogo 
    pygame.time.Clock().tick(10)

#encerramento do jogo 
pygame.quit()