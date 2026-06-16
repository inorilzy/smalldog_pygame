from __future__ import annotations

import random

import pygame

from utils.helper import resource_path


class GameBackground:
    def __init__(self, scene: pygame.Surface, speed: int = 1) -> None:
        self.image = pygame.image.load(resource_path("image/background.png")).convert()
        self.main_scene = scene
        self.speed = speed
        self.image_width = self.image.get_width()
        self.reset()

    def reset(self) -> None:
        self.x1 = 0
        self.x2 = self.image_width

    def action(self) -> None:
        self.x1 -= self.speed
        self.x2 -= self.speed

        if self.x1 <= -self.image_width:
            self.x1 = self.x2 + self.image_width
        if self.x2 <= -self.image_width:
            self.x2 = self.x1 + self.image_width

    def draw(self) -> None:
        self.main_scene.blit(self.image, (self.x1, 0))
        self.main_scene.blit(self.image, (self.x2, 0))


class Snow:
    def __init__(self, width: int = 1280, height: int = 390) -> None:
        self.width = width
        self.height = height
        self.reset()

    def reset(self) -> None:
        self.x = random.randint(0, self.width)
        self.y = random.randint(0, self.height)
        self.vx = random.randint(-3, 3)
        self.vy = 1

    def update(self) -> None:
        self.x += self.vx
        self.y += self.vy

        if self.y > self.height:
            self.y = 0
            self.x = random.randint(0, self.width)

        if self.x < 0:
            self.x = self.width
        elif self.x > self.width:
            self.x = 0

    def getsnowpos(self) -> tuple[int, int]:
        return self.x, self.y
