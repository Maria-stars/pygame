import pygame
def inicializa():
    pygame.init()

    window = pygame.display.set_mode((320, 240))
    pygame.display.set_caption("Jogo da Maria Eduarda dos Santos")

    return window

def recebe_eventos():

    game = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    return game

def desenha (window):
    pygame.display.update()
    tela = window.fill((255, 0, 0))
    return tela
    
def game_loop(window):

    game = True

# ===== Loop principal =====
    while game:
        # ----- Trata eventos
        game = recebe_eventos()
        if game:
            # ----- Gera saídas
            desenha(window)






