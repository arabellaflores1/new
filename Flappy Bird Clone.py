import pygame
import sys

# Инициализация Pygame
pygame.init()

# Настройки экрана
screen_width = 400
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flappy Bird Clone")

# Цвета
background_color = (135, 206, 250)
bird_color = (255, 255, 0)
pipe_color = (0, 128, 0)

# Параметры птицы
bird_radius = 20
bird_x = 100
bird_y = screen_height // 2
bird_velocity = 0
bird_gravity = 0.5

# Параметры труб
pipe_width = 50
pipe_gap = 150
pipe_velocity = 2
pipes = []

# Функция для отрисовки птицы и труб
def draw():
    screen.fill(background_color)
    
    pygame.draw.circle(screen, bird_color, (bird_x, bird_y), bird_radius)
    
    for pipe in pipes:
        pygame.draw.rect(screen, pipe_color, pipe)

    pygame.display.update()

# Основной игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bird_velocity = -10
    
    # Обновление параметров птицы
    bird_velocity += bird_gravity
    bird_y += bird_velocity
    
    # Генерация новых труб
    if len(pipes) == 0 or pipes[-1].right < screen_width - 200:
        pipe_height = pygame. randint(100, 400)
        pipe_rect_upper = pygame.Rect(screen_width, 0, pipe_width, pipe_height)
        pipe_rect_lower = pygame.Rect(screen_width, pipe_height + pipe_gap, pipe_width, screen_height - pipe_height - pipe_gap)
        pipes.append(pipe_rect_upper)
        pipes.append(pipe_rect_lower)
    
    # Обновление позиции труб и удаление невидимых труб
    for pipe in pipes:
        pipe.x -= pipe_velocity
        if pipe.right < 0:
            pipes.remove(pipe)
    
    # Проверка на столкновение с трубами
    for pipe in pipes:
        if pipe.colliderect((bird_x - bird_radius, bird_y - bird_radius, 2 * bird_radius, 2 * bird_radius)):
            pygame.quit()
            sys.exit()

    # Отрисовка
    draw()
    
    pygame.time.Clock().tick(60)
