from __future__ import annotations

from app.animated_sprite import AnimatedSprite


class MySprite(AnimatedSprite):
    def __init__(self, bounds_width: int = 1280, ground_y: int = 290) -> None:
        super().__init__(frame_rate=45)
        self.movieRight = False
        self.movieLeft = False
        self.speed = 7
        self.vUP = 0.0
        self.jumping = False
        self.bounds_width = bounds_width
        self.ground_y = ground_y

    def start_jump(self) -> None:
        if not self.jumping:
            self.jumping = True
            self.vUP = -14

    def update_jump(self) -> None:
        if not self.jumping:
            return

        if self.vUP < 0:
            self.vUP += 0.6
        else:
            self.vUP += 0.8

        self.Y += int(self.vUP)
        if self.Y >= self.ground_y:
            self.jumping = False
            self.Y = self.ground_y
            self.vUP = 0.0

    def reset(self) -> None:
        self.movieRight = False
        self.movieLeft = False
        self.jumping = False
        self.vUP = 0.0
        self.X = 0
        self.Y = self.ground_y

    def update(self, current_time: int, rate: int = 45) -> None:
        self.animate(current_time, rate)

        if self.movieRight:
            self.X = min(self.X + self.speed, self.bounds_width - self.rect.width)

        if self.movieLeft:
            self.X = max(self.X - self.speed, 0)
