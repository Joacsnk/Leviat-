import pygame

pygame.mixer.init()


def tocar_musica(caminho: str, ):
    pygame.mixer.music.load(caminho)
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)


def parar_musica():
    pygame.mixer.music.stop()


def pausar_musica():
    pygame.mixer.music.pause()


def continuar_musica():
    pygame.mixer.music.unpause()