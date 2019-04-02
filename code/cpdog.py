import random
import pygame
from pygame.locals import *
from pygame.sprite import Sprite


class Monster(Sprite):
    def __init__(self,screen):
        super(Monster, self).__init__()
        self.smonster=pygame.image.load('../image/鸡腿.png')
        wid=random.randint(33,33)
        self.smonster=pygame.transform.scale(self.smonster, (wid, wid))
        self.rect=self.smonster.get_rect()
        self.screen=screen
        self.rect.centerx = random.randint(1200, 1250)
        self.rect.bottom = random.randint(170, 270)
        self.speedx=1

    def draw_monster(self):
        self.screen.blit(self.smonster,(self.rect.centerx,self.rect.bottom))

    def update(self, *args):
        self.rect.x -=self.speedx


class MySprite2(pygame.sprite.Sprite):
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
        # self.X=1280
        # self.Y=285

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
        self.X -= 5




