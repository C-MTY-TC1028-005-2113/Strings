import pygame

pygame.init()
pygame.mixer.init()


sonido_fondo = pygame.mixer.Sound("baaad.wav")
pygame.mixer.Sound.set_volume(sonido_fondo, 1)
pygame.mixer.Sound.play(sonido_fondo, -1)
pygame.mixer.Sound.play(sonido_fondo, loops=5, fade_ms=10_000)
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.fadeout(10000)

#pygame.mixer.music.pause()
#pygame.mixer.music.unpause()