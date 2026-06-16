from __future__ import annotations

import pygame

from utils.helper import resource_path


class Fontf:
    def __init__(self, screen: pygame.Surface) -> None:
        self.screen = screen
        self.font = pygame.font.Font(resource_path("font/msyh.ttc"), 40)
        self.font_medium = pygame.font.Font(resource_path("font/msyh.ttc"), 28)
        self.font_small = pygame.font.Font(resource_path("font/msyh.ttc"), 20)
        self.bg1 = pygame.image.load(resource_path("image/background.jpg")).convert()
        self.title = self.font.render("smalldog", True, (42, 45, 45))
        self.subtitle = self.font_medium.render("Run, jump, eat drumsticks.", True, (72, 85, 85))
        self.start_button = self.font.render("Start Game", True, (0, 0, 0))
        self.start_button_rect = self.start_button.get_rect(topleft=(520, 175))
        self.start_tips = [
            self.font_small.render("方向键左右移动，Space 跳跃。", True, (72, 85, 85)),
            self.font_small.render("吃鸡腿加分，碰到情侣狗三次就结束。", True, (72, 85, 85)),
            self.font_small.render("按 Enter 或点击 Start Game 开始。", True, (72, 85, 85)),
        ]
        self.game_over_title = self.font.render("Game Over!", True, (72, 85, 85))
        self.restart_tip = self.font_small.render("按 Enter 重新开始，Esc 退出。", True, (72, 85, 85))

    def beginpage(self) -> None:
        self.screen.blit(self.bg1, (0, 0))
        self.screen.blit(self.title, (520, 70))
        self.screen.blit(self.subtitle, (450, 125))
        self.screen.blit(self.start_button, self.start_button_rect)
        for index, tip in enumerate(self.start_tips):
            self.screen.blit(tip, (420, 250 + index * 30))

    def gameoverrrrrrrrr(self, score: int, level: int) -> None:
        final_score = self.font_medium.render(f"Final score: {score}", True, (72, 85, 85))
        final_level = self.font_small.render(f"Level reached: {level}", True, (72, 85, 85))
        self.screen.blit(self.game_over_title, (500, 150))
        self.screen.blit(final_score, (510, 215))
        self.screen.blit(final_level, (540, 255))
        self.screen.blit(self.restart_tip, (470, 300))

    def displayScore(self, score: int, hits: int = 0, max_hits: int = 3, level: int = 1) -> None:
        lives = max(max_hits - hits, 0)
        score_text = self.font_medium.render(f"Score {score}", True, (50, 50, 50))
        lives_text = self.font_small.render(f"Lives {lives}/{max_hits}", True, (50, 50, 50))
        level_text = self.font_small.render(f"Level {level}", True, (50, 50, 50))
        self.screen.blit(score_text, (10, 10))
        self.screen.blit(lives_text, (12, 48))
        self.screen.blit(level_text, (12, 75))
