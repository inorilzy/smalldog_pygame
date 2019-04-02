import pygame

class Sound():
    def __init__(self):
        pygame.mixer.music.load('../sound/baab.mp3')
        pygame.mixer.music.play()

