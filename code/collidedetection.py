#碰撞检测
import pygame


class Collide():
    def __init__(self):
        self.gamestatus=True
        self.snowflag=False
        self.dogflag=0
        self.score=0
        self.scoreup=200
        self.gameover=False
        self.count=0

    def dogs_cpdogs(self,dogs,cpdogs):
        boooooooooooooooool=pygame.sprite.groupcollide(dogs,cpdogs,False,True)
        if boooooooooooooooool:
            self.score += self.scoreup
            print(self.score)

    def dog_cpdog(self,dog,cpdog2s):
        booooooool=pygame.sprite.spritecollide(dog,cpdog2s,True)
        if booooooool:
            self.snowflag = True
            self.count += 1
            if self.count>=3:
                self.gameover=True
