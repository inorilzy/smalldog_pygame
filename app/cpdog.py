from __future__ import annotations

import random

import pygame

from app.animated_sprite import AnimatedSprite
from utils.helper import resource_path


class Monster(pygame.sprite.Sprite):
    def __init__(self, spawn_x: int = 1280, speed: int = 4) -> None:
        super().__init__()
        image = pygame.image.load(resource_path("image/鸡腿.png")).convert_alpha()
        width = random.randint(30, 36)
        self.image = pygame.transform.smoothscale(image, (width, width))
        self.rect = self.image.get_rect()
        self.rect.x = spawn_x
        self.rect.bottom = random.randint(170, 270)
        self.speedx = speed

    def update(self, *args) -> None:
        self.rect.x -= self.speedx
        if self.rect.right < 0:
            self.kill()


class MySprite2(AnimatedSprite):
    def __init__(self, speed: int = 5) -> None:
        super().__init__(frame_rate=45)
        self.speed = speed

    def update(self, current_time: int, rate: int = 45) -> None:
        self.animate(current_time, rate)
        self.X -= self.speed
        if self.rect.right < 0:
            self.kill()
