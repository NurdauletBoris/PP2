import pygame
import random
import sys
import os

pygame.init()
pygame.mixer.init()

#настройки экрана
WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("RACING")
clock = pygame.time.Clock()
BASE_DIR = os.path.dirname(__file__)

# Загрузка изображений
background = pygame.image.load(os.path.join(BASE_DIR, 'AnimatedStreet.png'))
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

player_img = pygame.image.load(os.path.join(BASE_DIR, 'Player.png'))
player_img = pygame.transform.scale(player_img, (60, 80))

enemy_img = pygame.image.load(os.path.join(BASE_DIR, 'Enemy.png'))
enemy_img = pygame.transform.scale(enemy_img, (60, 80))

coin_img = pygame.image.load(os.path.join(BASE_DIR, 'coin.png'))
coin_img = pygame.transform.scale(coin_img, (40, 40))

# Загрузка звуков
pygame.mixer.music.load(os.path.join(BASE_DIR, 'background.wav'))
crash_sound = pygame.mixer.Sound(os.path.join(BASE_DIR, 'crash.wav'))


#настройки игры
player_speed = 7
score = 0
font = pygame.font.SysFont("Arial", 30)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect(center=(WIDTH//2, HEIGHT-80))
        self.speed = player_speed

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed
        

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.reset()
        self.speed = random.randint(3, 6)

    def reset(self):
        self.rect.x = random.randint(40, WIDTH-100)
        self.rect.y = random.randint(-600, -100)

    def update(self, enemy_group):
        self.rect.y += self.speed
        
        #проверка столкновений с другими врагами
        for enemy in enemy_group:
            if enemy != self and self.rect.colliderect(enemy.rect):
                if self.rect.x < enemy.rect.x:
                    self.rect.x -= 5
                else:
                    self.rect.x += 5
                break
        
        if self.rect.top > HEIGHT:
            self.reset()
            self.speed = random.randint(3, 6)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = coin_img
        self.rect = self.image.get_rect()
        self.reset()

    def reset(self):
        self.rect.x = random.randint(40, WIDTH-80)
        self.rect.y = random.randint(-600, -100)

    def update(self):
        self.rect.y += 4
        if self.rect.top > HEIGHT:
            self.reset()

player = Player()
enemies = pygame.sprite.Group()
coins = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

all_sprites.add(player)

#создание 7 машинок
for _ in range(7):
    enemy = Enemy()
    enemies.add(enemy)
    all_sprites.add(enemy)

#создание 2 монеток
for _ in range(2):
    coin = Coin()
    coins.add(coin)
    all_sprites.add(coin)

pygame.mixer.music.play(-1)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #обновление
    player.update()
    enemies.update(enemies)
    coins.update()

    #отрисовка
    screen.blit(background, (0, 0))
    all_sprites.draw(screen)

    # счет
    score_text = font.render(f"Coins: {score}", True, (0, 0, 0))
    screen.blit(score_text, (WIDTH-120, 10))

    #проверка столкновений
    if pygame.sprite.spritecollide(player, enemies, False):
        crash_sound.play()
        pygame.time.delay(2000)
        running = False

    for coin in pygame.sprite.spritecollide(player, coins, True):
        score += 1
        new_coin = Coin()
        coins.add(new_coin)
        all_sprites.add(new_coin)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()