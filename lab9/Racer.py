import random
import sys
import pygame
from pygame.locals import *

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("Kavinsky_Nightcall.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play()

crash_sound = pygame.mixer.Sound("crash.wav")
speed_sound = pygame.mixer.Sound("zvuk-nachavsheysya-gonki-slyishen-iz-daleka.wav")
speed = 5

WHITE = (255, 255, 255)
WIDTH, HEIGHT = 400, 600

display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Racer")

background = pygame.image.load("AnimatedStreet.png")
background2 = pygame.image.load("MainpageDrive.png")

fps = 60
FPS = pygame.time.Clock()

game_over_font = pygame.font.SysFont("Times New Roman", 50)
font = pygame.font.SysFont("Times New Roman", 25)

class Enemy1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("car2.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, WIDTH - 40), 0)

    def move(self):
        self.rect.move_ip(0, 10)
        if self.rect.top > HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(40, WIDTH - 40), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
"""
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("")
        self.rect = self.image.get_rect()
        self.rect.center = 
"""





class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("car1.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[K_w] or keys[K_UP]:
            self.rect.move_ip(0, -5)
            speed_sound.play()
            speed_sound.set_volume(0.1)
        if keys[K_s] or keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if self.rect.left > 0 and (keys[K_LEFT] or keys[K_a]):
            self.rect.move_ip(-5, 0)
        if self.rect.right < WIDTH and (keys[K_RIGHT] or keys[K_d]):
            self.rect.move_ip(5, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


P1 = Player()
E1 = Enemy1()

score = 0
game_over = False
start_game = False

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if not start_game and event.type == KEYDOWN and event.key == K_RETURN:
            start_game = True
            pygame.mixer.music.stop()
        if game_over and event.type == KEYDOWN and event.key == K_SPACE:
            P1 = Player()
            E1 = Enemy1()
            score = 0
            game_over = False
            pygame.mixer.music.play(-1)
            
    if not start_game:
        display.blit(background2, (0, 0))
        title_text = game_over_font.render("GAME RACER", True, (255, 255, 255))
        start_text = font.render("Нажмите ENTER для старта", True, (255, 255, 255))
        display.blit(title_text, (WIDTH // 2 - 150, HEIGHT // 2 - 50))
        display.blit(start_text, (WIDTH // 2 - 150, HEIGHT // 2 + 10))

    else:
        if not game_over:
            display.blit(background, (0, 0))

            P1.move()
            P1.draw(display)

            E1.move()
            E1.draw(display)

            score += 1
            score_text = font.render(f"Score: {score}", True, (0,0,0))
            display.blit(score_text, (10, 10))

            if pygame.sprite.collide_rect(P1, E1):
                pygame.mixer.music.stop()
                speed_sound.stop()
                crash_sound.play()
                game_over = True
        else:
            game_over_text = game_over_font.render("Game over", True, (255, 0, 0))
            score_text = font.render(f"Final Score: {score}", True, (0, 0, 0))
            restart_game = font.render(f"Press SPACE restart game.", True, (0, 0, 0))
            display.fill(WHITE)
            display.blit(game_over_text, (WIDTH // 2 - 90, HEIGHT // 2 - 40))
            display.blit(score_text, (WIDTH // 2 - 70, HEIGHT //  2 + 20))
            display.blit(restart_game, (WIDTH // 2 - 140, HEIGHT // 2 + 50))
    pygame.display.update()
    FPS.tick(fps)
