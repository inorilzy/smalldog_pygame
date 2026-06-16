from __future__ import annotations

import pygame


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, frame_rate: int = 45) -> None:
        super().__init__()
        self.image: pygame.Surface | None = None
        self.master_image: pygame.Surface | None = None
        self.rect = pygame.Rect(0, 0, 1, 1)
        self.frame = 0
        self.old_frame = -1
        self.frame_width = 1
        self.frame_height = 1
        self.first_frame = 0
        self.last_frame = 0
        self.columns = 1
        self.last_time = 0
        self.frame_rate = frame_rate

    @property
    def X(self) -> int:
        return self.rect.x

    @X.setter
    def X(self, value: int) -> None:
        self.rect.x = value

    @property
    def Y(self) -> int:
        return self.rect.y

    @Y.setter
    def Y(self, value: int) -> None:
        self.rect.y = value

    def load(self, filename: str, width: int, height: int, columns: int) -> None:
        self.master_image = pygame.image.load(filename).convert_alpha()
        self.frame_width = width
        self.frame_height = height
        self.columns = columns
        self.rect = pygame.Rect(0, 0, width, height)
        rect = self.master_image.get_rect()
        self.last_frame = (rect.width // width) * (rect.height // height) - 1
        self._render_current_frame()

    def animate(self, current_time: int, rate: int | None = None) -> None:
        if self.master_image is None:
            return

        animation_rate = rate or self.frame_rate
        if current_time > self.last_time + animation_rate:
            self.frame += 1
            if self.frame > self.last_frame:
                self.frame = self.first_frame
            self.last_time = current_time

        if self.frame != self.old_frame:
            self._render_current_frame()

    def _render_current_frame(self) -> None:
        if self.master_image is None:
            return

        frame_x = (self.frame % self.columns) * self.frame_width
        frame_y = (self.frame // self.columns) * self.frame_height
        rect = (frame_x, frame_y, self.frame_width, self.frame_height)
        self.image = self.master_image.subsurface(rect)
        self.old_frame = self.frame
