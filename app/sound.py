from __future__ import annotations

import pygame

from utils.helper import resource_path


class Sound:
    def __init__(self) -> None:
        self.available = False

        try:
            if not pygame.mixer.get_init():
                pygame.mixer.init()
            pygame.mixer.music.load(resource_path("sound/baab.mp3"))
            pygame.mixer.music.play(-1)
            self.available = True
        except pygame.error:
            self.available = False
