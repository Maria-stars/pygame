import pygame  
from random import randint

def inicializa():
    pygame.init()

    window = pygame.display.set_mode((320, 240))
    pygame.display.set_caption("Jogo da Maria Eduarda dos Santos")
    assets = {"nave": pygame.image.load("assets/img/playerShip1_orange.png"), 
              "fundo": pygame.image.load("assets/img/starfield.png")
                }
    
    return window, assets

def recebe_eventos():

    game = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    return game

def desenha (window, assets):
    pygame.display.update()
    tela = window.fill((255, 0, 0))
    window.blit(assets["nave"], (160,240))  
    window.blit(assets["fundo"], (0,0))  
    pygame.draw.circle(window, (255,255,255), (randint(0,320), randint(0,240)), 2)

    return tela
    
def game_loop(window, assets):

    game = True

# ===== Loop principal =====
    while game:
        # ----- Trata eventos
        game = recebe_eventos()
        if game:
            # ----- Gera saídas
            desenha(window, assets)

if __name__ == '__main__':
    window, assets= inicializa()
    game_loop(window, assets)