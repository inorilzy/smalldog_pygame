from __future__ import annotations

from app.animated_sprite import AnimatedSprite


class MySpritec(AnimatedSprite):
    def __init__(self, speed: int = 7, screen_width: int = 1280) -> None:
        super().__init__(frame_rate=50)
        self.movieRight = True
        self.speed = speed
        self.screen_width = screen_width

    def update(self, current_time: int, rate: int = 50) -> None:
        self.animate(current_time, rate)
        if self.movieRight:
            self.X += self.speed

    def has_left_screen(self) -> bool:
        return self.rect.left > self.screen_width
