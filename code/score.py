import pygame



class Fontf():
    def __init__(self,screen):
        self.screen=screen
        self.font=pygame.font.Font('../font/msyh.ttc',40)   #字体，30大小,生成对象
        self.font2 = pygame.font.Font('../font/msyh.ttc', 20)
        self.bg1=pygame.image.load('../image/background.jpg')
        self.font_text1 = self.font.render('start game ', True, (0, 0, 0))
        textrect=self.font_text1.get_rect()
        self.text_width=textrect.right
        self.text_height=textrect.height

        self.font_text_startgame=self.font2.render('我是一只快乐的单身狗，<- -> space 控制我移动跳跃；', True, (72, 85, 85))
        self.font_text_startgame2=self.font2.render('我可以吃鸡腿，不能离情侣狗太近，会吃到成吨的狗粮，立刻去世！', True, (72, 85, 85))
        self.font_text_gameover = self.font.render('game over !', True, (72, 85, 85))
        self.font_text_gameover2 = self.font.render('我是一只悲伤的单身狗，我不活了！', True, (72, 85, 85))

    def beginpage(self):
        self.screen.blit(self.bg1, (0, 0))
        self.screen.blit(self.font_text1,(540,180))
        self.screen.blit(self.font_text_startgame, (450, 250))
        self.screen.blit(self.font_text_startgame2, (450, 280))

    def gameoverrrrrrrrr(self):
        self.screen.blit(self.font_text_gameover, (540, 180))
        self.screen.blit(self.font_text_gameover2, (380, 240))

    def displayScore(self,score):
        self.score=score
        self.font_text2 = self.font.render('score:' + str(self.score), True, (200, 100, 200))
        self.screen.blit(self.font_text2, (0,0))

