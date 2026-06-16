from __future__ import annotations

import os
import random
from enum import Enum, auto

import pygame

from app.background import GameBackground, Snow
from app.collidedetection import Collide
from app.cpdog import Monster, MySprite2
from app.crydog import MySpritec
from app.dog import MySprite
from app.score import Fontf
from app.sound import Sound
from utils.helper import resource_path

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 390
GROUND_Y = 285
PLAYER_GROUND_Y = 290
FPS = 60
SNOW_COUNT = 50
SPAWN_INTERVAL_MIN_MS = 1000
SPAWN_INTERVAL_MAX_MS = 3000
SCORE_STEP_MS = 100
LEVEL_SCORE_STEP = 500
MAX_LEVEL = 9


class GameState(Enum):
    MENU = auto()
    PLAYING = auto()
    GAME_OVER = auto()


class SmallDogGame:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("smalldog")
        self.clock = pygame.time.Clock()
        self.background = GameBackground(self.screen)
        self.collidetest = Collide()
        self.sound = Sound()
        self.scoreboard = Fontf(self.screen)
        self.snowlist = [Snow(SCREEN_WIDTH, SCREEN_HEIGHT) for _ in range(SNOW_COUNT)]
        self.state = GameState.MENU
        self.next_spawn_at = 0
        self.score_timer = 0
        self.crydogs = pygame.sprite.Group()
        self.crydog = None

        self.dog = MySprite(bounds_width=SCREEN_WIDTH, ground_y=PLAYER_GROUND_Y)
        self.dog.load(resource_path("image/dog.png"), 82, 62, 3)
        self.dogs = pygame.sprite.Group(self.dog)
        self.collectibles = pygame.sprite.Group()
        self.cpdog2s = pygame.sprite.Group()
        self.dog.reset()

    def difficulty_level(self) -> int:
        return min(self.collidetest.score // LEVEL_SCORE_STEP + 1, MAX_LEVEL)

    def obstacle_speed(self) -> int:
        return 4 + self.difficulty_level()

    def spawn_interval(self) -> int:
        level = self.difficulty_level()
        min_interval = max(450, SPAWN_INTERVAL_MIN_MS - (level - 1) * 70)
        max_interval = max(900, SPAWN_INTERVAL_MAX_MS - (level - 1) * 180)
        return random.randint(min_interval, max_interval)

    def start_game(self) -> None:
        self.state = GameState.PLAYING
        self.collidetest.reset()
        self.background.reset()
        self.background.speed = 1
        self.collectibles.empty()
        self.cpdog2s.empty()
        self.crydogs.empty()
        self.crydog = None
        self.dog.reset()
        self.score_timer = 0
        self.next_spawn_at = pygame.time.get_ticks() + self.spawn_interval()

    def spawn_obstacles(self) -> None:
        spawn_x = SCREEN_WIDTH + random.randint(0, 60)
        speed = self.obstacle_speed()

        monster = Monster(spawn_x=spawn_x, speed=max(speed - 1, 4))
        self.collectibles.add(monster)

        cpdog2 = MySprite2(speed=speed)
        cpdog2.load(resource_path("image/cpdogs.png"), 113, 62, 3)
        cpdog2.X = spawn_x
        cpdog2.Y = GROUND_Y
        self.cpdog2s.add(cpdog2)

    def ensure_game_over_sprite(self) -> None:
        if self.crydog is not None:
            return

        self.crydog = MySpritec(screen_width=SCREEN_WIDTH)
        self.crydog.load(resource_path("image/crydog.png"), 82, 62, 3)
        self.crydog.X = 100
        self.crydog.Y = GROUND_Y
        self.crydogs.add(self.crydog)

    def handle_event(self, event: pygame.event.Event) -> bool:
        if event.type == pygame.QUIT:
            return False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False

            if self.state in (GameState.MENU, GameState.GAME_OVER) and event.key in (pygame.K_RETURN, pygame.K_SPACE):
                self.start_game()
                return True

            if self.state == GameState.PLAYING:
                if event.key == pygame.K_RIGHT:
                    self.dog.movieRight = True
                elif event.key == pygame.K_LEFT:
                    self.dog.movieLeft = True
                elif event.key == pygame.K_SPACE:
                    self.dog.start_jump()

        if event.type == pygame.KEYUP and self.state == GameState.PLAYING:
            if event.key == pygame.K_RIGHT:
                self.dog.movieRight = False
            elif event.key == pygame.K_LEFT:
                self.dog.movieLeft = False

        if event.type == pygame.MOUSEBUTTONDOWN and self.state == GameState.MENU:
            if self.scoreboard.start_button_rect.collidepoint(event.pos):
                self.start_game()

        return True

    def update_score(self, delta_ms: int) -> None:
        self.score_timer += delta_ms
        while self.score_timer >= SCORE_STEP_MS:
            self.collidetest.score += 1
            self.score_timer -= SCORE_STEP_MS

    def update_snow(self) -> None:
        for snow in self.snowlist:
            snow.update()

    def draw_snow(self) -> None:
        for snow in self.snowlist:
            pygame.draw.circle(self.screen, (255, 255, 255), snow.getsnowpos(), 1)

    def update_playing(self, current_time: int, delta_ms: int) -> None:
        self.background.speed = min(1 + self.difficulty_level() // 3, 4)
        self.background.action()
        self.dog.update_jump()
        self.collidetest.dogs_cpdogs(self.dogs, self.collectibles)
        self.collidetest.dog_cpdog(self.dog, self.cpdog2s)
        self.update_score(delta_ms)

        self.dogs.update(current_time)
        self.collectibles.update()
        self.cpdog2s.update(current_time)

        if current_time >= self.next_spawn_at:
            self.spawn_obstacles()
            self.next_spawn_at = current_time + self.spawn_interval()

        if self.collidetest.snowflag:
            self.update_snow()

        if self.collidetest.gameover:
            self.state = GameState.GAME_OVER
            self.ensure_game_over_sprite()

    def update_game_over(self, current_time: int) -> None:
        self.background.action()
        if self.collidetest.snowflag:
            self.update_snow()
        self.ensure_game_over_sprite()
        self.crydogs.update(current_time)

    def draw(self) -> None:
        if self.state == GameState.MENU:
            self.scoreboard.beginpage()
            pygame.display.update()
            return

        self.background.draw()

        if self.collidetest.snowflag:
            self.draw_snow()

        if self.state == GameState.PLAYING:
            self.collectibles.draw(self.screen)
            self.cpdog2s.draw(self.screen)
            self.dogs.draw(self.screen)
        else:
            self.crydogs.draw(self.screen)
            self.scoreboard.gameoverrrrrrrrr(self.collidetest.score, self.difficulty_level())

        self.scoreboard.displayScore(
            self.collidetest.score,
            self.collidetest.count,
            self.collidetest.game_over_hits,
            self.difficulty_level(),
        )
        pygame.display.update()

    def run(self, max_frames: int | None = None) -> int:
        running = True
        frame_count = 0

        while running:
            delta_ms = self.clock.tick(FPS)
            current_time = pygame.time.get_ticks()

            for event in pygame.event.get():
                running = self.handle_event(event)
                if not running:
                    break

            if self.state == GameState.PLAYING:
                self.update_playing(current_time, delta_ms)
            elif self.state == GameState.GAME_OVER:
                self.update_game_over(current_time)

            self.draw()
            frame_count += 1

            if max_frames is not None and frame_count >= max_frames:
                break

        pygame.quit()
        return 0


def main() -> int:
    max_frames = os.getenv("SMALLDOG_HEADLESS_TEST_FRAMES")
    game = SmallDogGame()
    return game.run(int(max_frames)) if max_frames else game.run()


if __name__ == "__main__":
    raise SystemExit(main())
