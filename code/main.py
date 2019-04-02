import pygame
import sys,os
import random
from background import GameBackground,Snow
from dog import MySprite
from cpdog import Monster,MySprite2
from pygame.sprite import Group
from collidedetection import Collide
from sound import Sound
from score import Fontf
from crydog import MySpritec


pygame.init()
screen=pygame.display.set_mode((1280,390))
fpsset=pygame.time.Clock()
bgcolor=(255,240,30)
background=GameBackground(screen)
dog=MySprite() 
dog.load("../image/dog.png", 82, 62, 3)
dog.X = 0
dog.Y = 285
dogs = pygame.sprite.Group()
dogs.add(dog)
cpdogs=Group()
lasttimecreat=0
collidetest=Collide()
sound=Sound()
cpdog2s = pygame.sprite.Group()
snowlist = []
for i in range(0, 50):  # 建立50个雪花
    snow=Snow()
    snowlist.append(snow)
scor=Fontf(screen)
onoff = True
crydog=None


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # player ctrl
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                dog.movieRight=True
            if event.key == pygame.K_LEFT:
                dog.movieLeft=True
            if event.key==pygame.K_SPACE:
                if not dog.jumping:
                    dog.jumping=True
                    dog.vUP = -14
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                dog.movieRight=False
            if event.key==pygame.K_LEFT:
                dog.movieLeft=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            mousex,mousey=pygame.mouse.get_pos()
            if mousex>=540 and mousex<=540 + scor.text_width:
                if mousey>=180 and mousey<=180 + scor.text_height:
                    onoff = False
    if dog.jumping:
        if dog.vUP < 0:
            dog.vUP += 0.6
        elif dog.vUP >= 0:
            dog.vUP += 0.8
        dog.Y += dog.vUP
        if dog.Y >= 290:
            dog.jumping = False
            dog.Y = 290
            dog.vUP = 0.0
    if not collidetest.gameover:

        if onoff:
            scor.beginpage()
            print(onoff)

        else:
            print(onoff)

        #碰撞检测
            collidetest.dogs_cpdogs(dogs,cpdogs)
            collidetest.dog_cpdog(dog,cpdog2s)
            #背景
            background.action()
            background.draw()
            #分数
            # scor.beginpage()
            collidetest.score+=1
            scor.displayScore(collidetest.score)
            #时间控制
            ticks = pygame.time.get_ticks()
            #player绘制
            dogs.update(ticks)
            dogs.draw(screen)

            cpdog2s.update(ticks)
            cpdog2s.draw(screen)
            if ticks >lasttimecreat  + random.randint(1000,20000):
                 #生成障碍物
                cp = Monster(screen)
                cpdogs.add(cp)
                cpdog2 = MySprite2()
                cpdog2.load("../image/cpdogs.png", 113, 62, 3)
                cpdog2.X = 1280
                cpdog2.Y = 285
                cpdog2s.add(cpdog2)
                lasttimecreat=ticks

            for m in cpdogs:
                m.draw_monster()
                if m.rect.x <=640:
                    del m
            cpdogs.update()

        #snow
            if collidetest.snowflag:
                for snow in snowlist:
                    # 每个雪花位置的变换
                    # if random.randint(0,1):
                    snow.vx = random.randint(-3,3)  # 雪花的横向速度
                    snow.vy = 1                     # 雪花的竖直速度
                    snow.x += snow.vx               # 雪花的横轴移动位置
                    snow.y += snow.vy               # 雪花的纵轴移动位置
                    if snow.y > 500:
                        snow.y = 0
                    pygame.draw.circle(screen,[255,255,255],snow.getsnowpos(),1)
    else:
        if collidetest.snowflag:
            background.action()
            background.draw()
            for snow in snowlist:
                snow.vx = random.randint(-3, 3)
                snow.vy = 1
                snow.x += snow.vx
                snow.y += snow.vy
                if snow.y > 500:
                    snow.y = 0
                pygame.draw.circle(screen, [255, 255, 255], snow.getsnowpos(), 1)
            if not crydog:
                crydog=MySpritec()
                crydog.load("../image/crydog.png", 82, 62,3)
                crydog.X = 100
                crydog.Y = 285
                crydogs=Group()
                crydogs.add(crydog)
            ticks = pygame.time.get_ticks()
            # player绘制
            crydogs.update(ticks)
            crydogs.draw(screen)
            scor.gameoverrrrrrrrr()
            if crydog.X>1280:
                sys.exit()
    fpsset.tick(60)
    pygame.display.update()
