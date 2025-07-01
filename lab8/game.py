import pygame
pygame.init()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Image")
clock = pygame.time.Clock()

player = pygame.image.load("ритейк.jpeg")

player = pygame.transform.scale(player, (100, 100))

enemy_frames = []

for i in range(1, 5):
    frame = pygame.image.load(f"robots{i}.png")
    frame = pygame.transform.scale(frame, (200, 200))
    enemy_frames.append(frame)

for i in range(1, 7):
    frame2 = pygame.image.load(f"robots_attack{i}.png")
    frame2 = pygame.transform.scale(frame2, (200, 200))
    enemy_frames.append(frame2)

frame_index = 0
frame_index2 = 2
frame_speed = 10
frame_timer = 0
enemy_x, enemy_y = 300, 300
#enemy_x2, enemy_y2 = 100, 500

x, y = 100, 100
speed = 3

running = True

while running:
    screen.fill((200, 200, 200))
    screen.blit(player, (x, y))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        x -= speed
        #x2 -= speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        x += speed
        #x2 += speed
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        y += speed
        #y2 += speed
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        y -= speed
        #y2 -= speed
    if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
        speed = 10
    else:
        speed = 5

    frame_timer += 1
    if frame_timer >= frame_speed:
        frame_timer = 0
        frame_index = (frame_index + 1) % len(enemy_frames)

    screen.blit(enemy_frames[frame_index], (enemy_x, enemy_y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60)
pygame.quit()