import pygame
import sys
pygame.init()
WIDTH, HEIGHT = 800, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (192, 192, 192)
DARK_GRAY = (64, 64, 64)
CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)
DARK_GREEN = (0, 100, 0)
LIGHT_BLUE = (173, 216, 230)
LIGHT_RED = (255, 182, 193)
GOLD = (255, 215, 0)
BALL_COLOR = (255, 0, 255)
BLOCK_SIZE = 40
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Numbered Grid Game")
clock = pygame.time.Clock()
grid = [[0 for _ in range(20)] for _ in range(15)]
ball_radius = BLOCK_SIZE // 2
ball_x, ball_y = WIDTH // 2, ball_radius * 2
ball_speed = 5
falling = True
rolling = False
selected_block = None
running = True
while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                selected_block = YELLOW
            elif event.key == pygame.K_2:
                selected_block = GREEN
            elif event.key == pygame.K_3:
                selected_block = BLUE
            elif event.key == pygame.K_4:
                selected_block = RED
            elif event.key == pygame.K_5:
                selected_block = ORANGE
            elif event.key == pygame.K_6:
                selected_block = PURPLE
            elif event.key == pygame.K_7:
                selected_block = DARK_GREEN
            elif event.key == pygame.K_8:
                selected_block = LIGHT_BLUE
            elif event.key == pygame.K_9:
                selected_block = LIGHT_RED
            elif event.key == pygame.K_0:
                selected_block = None  # Auswahl aufheben
            elif event.key == pygame.K_q:
                selected_block = BLACK
            elif event.key == pygame.K_w:
                selected_block = WHITE
            elif event.key == pygame.K_e:
                selected_block = GRAY
            elif event.key == pygame.K_r:
                selected_block = CYAN
            elif event.key == pygame.K_t:
                selected_block = GOLD
            elif event.key == pygame.K_z:
                selected_block = DARK_GRAY
            elif event.key == pygame.K_u:
                rolling = False
                ball_x, ball_y = pygame.mouse.get_pos()
                ball_y -= ball_radius * 2
                pygame.draw.circle(screen, BALL_COLOR, (ball_x, ball_y), ball_radius)
            elif event.key == pygame.K_SPACE:
                mouse_pos = pygame.mouse.get_pos()
                x = mouse_pos[0] // BLOCK_SIZE
                y = mouse_pos[1] // BLOCK_SIZE
                if 0 <= x < 20 and 0 <= y < 15:
                    grid[y][x] = selected_block
    if not falling and not rolling:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            ball_x -= ball_speed
        if keys[pygame.K_RIGHT]:
            ball_x += ball_speed
    if not rolling:
        if ball_y < HEIGHT - ball_radius * 2:
            falling = True
            ball_y += ball_speed
        else:
            falling = False
    ball_rect = pygame.Rect(ball_x - ball_radius, ball_y - ball_radius, ball_radius * 2, ball_radius * 2)
    for i in range(20):
        for j in range(15):
            if grid[j][i]:
                block_rect = pygame.Rect(i * BLOCK_SIZE, j * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
                if ball_rect.colliderect(block_rect):
                    if ball_y < block_rect.centery:
                        ball_y = block_rect.top - ball_radius
                        falling = False
                    elif ball_x < block_rect.centerx:
                        ball_x = block_rect.left - ball_radius
                    else:
                        ball_x = block_rect.right + ball_radius
    for i in range(20):
        for j in range(15):
            rect = pygame.Rect(i * BLOCK_SIZE, j * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, WHITE, rect, 1)
            if grid[j][i]:
                pygame.draw.rect(screen, grid[j][i], rect)
    if selected_block:
        pygame.draw.rect(screen, selected_block, pygame.mouse.get_pos() + (BLOCK_SIZE, BLOCK_SIZE))
    pygame.display.flip()
    clock.tick(30)
pygame.quit()
sys.exit()