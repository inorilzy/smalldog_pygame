import pygame
from pygame.locals import *
from pygame.sprite import Sprite


class MySprite(pygame.sprite.Sprite):
    def __init__(self, target=None):
        pygame.sprite.Sprite.__init__(self)
        # self.target_surface = target
        self.image = None
        self.master_image = None
        self.rect = None
        self.frame = 0
        self.old_frame = -1
        self.frame_width = 1
        self.frame_height = 1
        self.first_frame = 0
        self.last_frame = 0
        self.columns = 1
        self.last_time = 0
        self.movieRight = False
        self.movieLeft = False
        self.movieUp = False
        self.movieDown = True
        self.speed=7
        self.vUP=0  #纵向向上速度
        self.jumping=False

    def _getx(self): return self.rect.x
    def _setx(self, value): self.rect.x = value
    X = property(_getx, _setx)

    def _gety(self): return self.rect.y
    def _sety(self, value): self.rect.y = value
    Y = property(_gety, _sety)

    def load(self, filename, width, height, columns):
        self.master_image = pygame.image.load(filename).convert_alpha()
        self.frame_width = width
        self.frame_height = height
        # self.rect = self.x, self.y, width, height
        self.columns = columns
        self.rect = Rect(0, 0, width, height)
        rect = self.master_image.get_rect()
        self.last_frame = (rect.width // width) * (rect.height // height) - 1

    def update(self, current_time, rate=45):
        if current_time > self.last_time + rate:
            self.frame += 1
            if self.frame > self.last_frame:
                self.frame = self.first_frame
            self.last_time = current_time
        if self.frame != self.old_frame:
            frame_x = (self.frame % self.columns) * self.frame_width
            frame_y = (self.frame // self.columns) * self.frame_height
            rect = (frame_x, frame_y, self.frame_width, self.frame_height)
            self.image = self.master_image.subsurface(rect)
            self.old_frame = self.frame
        if self.movieRight:
            self.X += self.speed
            if self.X > 1280:
                self.X = 1280
        if self.movieLeft:
            self.X -= self.speed
            if self.X < 0:
                self.X = 0
