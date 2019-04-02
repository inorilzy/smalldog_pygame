#地图滚动
import pygame
import random

class GameBackground(object):
    # 初始化地图
    def __init__(self, scene):
        # 加载相同张图片资源,做交替实现地图滚动
        self.image1 = pygame.image.load("../image/background.png")
        self.image2 = pygame.image.load("../image/background.png")
        # 保存场景对象
        self.main_scene = scene
        # 辅助移动地图
        self.x1 = 0
        self.x2 = 1280
        self.snowflag=False

    # 计算地图图片绘制坐标
    def action(self):
        self.x1 = self.x1 - 1
        self.x2 = self.x2 - 1
        if self.x1 <= -1279:
            self.x1 = 1279
        if self.x2 <= -1279:
            self.x2 = 1279

    # 绘制地图的两张图片
    def draw(self):
        self.main_scene.blit(self.image1, (self.x1,0))
        self.main_scene.blit(self.image2, (self.x2,0))


class Snow():
                # 雪花的竖直速度
    def __init__(self):
        self.x = 0  # 雪花的横坐标
        self.y = 0  # 雪花的纵坐标
        self.vx = 0  # 雪花的水平速度
        self.vy = 0
        self.x = random.randint(0,1280)   # 初始化雪花横坐标
        self.y = random.randint(0,390)   #初始化雪花纵坐标
    def getsnowpos(self):
        return self.x,self.y         # 返回雪花坐标位置