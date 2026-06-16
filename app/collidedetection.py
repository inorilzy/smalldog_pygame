from __future__ import annotations

import pygame


class Collide:
    def __init__(self, game_over_hits: int = 3, bonus_score: int = 200) -> None:
        self.game_over_hits = game_over_hits
        self.bonus_score = bonus_score
        self.reset()

    def reset(self) -> None:
        self.snowflag = False
        self.score = 0
        self.gameover = False
        self.count = 0

    def dogs_cpdogs(self, dogs: pygame.sprite.Group, cpdogs: pygame.sprite.Group) -> int:
        collisions = pygame.sprite.groupcollide(dogs, cpdogs, False, True)
        if not collisions:
            return 0

        gained_score = sum(len(items) for items in collisions.values()) * self.bonus_score
        self.score += gained_score
        return gained_score

    def dog_cpdog(self, dog: pygame.sprite.Sprite, cpdog2s: pygame.sprite.Group) -> bool:
        hits = pygame.sprite.spritecollide(dog, cpdog2s, True)
        if not hits:
            return False

        self.snowflag = True
        self.count += len(hits)
        if self.count >= self.game_over_hits:
            self.gameover = True

        return True
