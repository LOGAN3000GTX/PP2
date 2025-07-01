import pygame
import sys
import random

# Инициализация
pygame.init()
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game with Levels")
clock = pygame.time.Clock()

# Цвета
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Шрифт
font = pygame.font.SysFont("Arial", 24)

# Стартовые параметры
snake = [(100, 100), (80, 100), (60, 100)]  # тело змеи
direction = 'RIGHT'
food = None
score = 0
level = 1
speed = 10  # начальная скорость

# Игровая сетка (границы)
COLS = WIDTH // CELL_SIZE
ROWS = HEIGHT // CELL_SIZE

def draw_grid():
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, BLACK, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, BLACK, (0, y), (WIDTH, y))

def draw_snake():
    for part in snake:
        pygame.draw.rect(screen, GREEN, (*part, CELL_SIZE, CELL_SIZE))

def draw_food():
    pygame.draw.rect(screen, RED, (*food, CELL_SIZE, CELL_SIZE))

def show_info():
    score_text = font.render(f"Score: {score}  Level: {level}", True, BLUE)
    screen.blit(score_text, (10, 10))

def generate_food():
    while True:
        x = random.randint(0, COLS - 1) * CELL_SIZE
        y = random.randint(0, ROWS - 1) * CELL_SIZE
        if (x, y) not in snake:
            return (x, y)

# Стартовая еда
food = generate_food()

# Главный цикл
while True:
    screen.fill(WHITE)
    draw_grid()
    draw_snake()
    draw_food()
    show_info()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Изменение направления
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                direction = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                direction = 'DOWN'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                direction = 'RIGHT'

    # Движение змеи
    head_x, head_y = snake[0]
    if direction == 'UP':
        head_y -= CELL_SIZE
    elif direction == 'DOWN':
        head_y += CELL_SIZE
    elif direction == 'LEFT':
        head_x -= CELL_SIZE
    elif direction == 'RIGHT':
        head_x += CELL_SIZE

    new_head = (head_x, head_y)

    # Проверка выхода за границу (стены)
    if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
        pygame.quit()
        sys.exit()

    # Проверка на самопересечение
    if new_head in snake:
        pygame.quit()
        sys.exit()

    # Обновление тела змеи
    snake.insert(0, new_head)

    # Проверка еды
    if new_head == food:
        score += 1
        food = generate_food()

        # Уровень повышается каждые 4 очка
        if score % 4 == 0:
            level += 1
            speed += 2  # ускоряем
    else:
        snake.pop()  # удаляем хвост, если не еда

    pygame.display.update()
    clock.tick(speed)
