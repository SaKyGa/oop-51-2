import pygame
import random
import os

# Инициализация Pygame
pygame.init()

# Размеры экрана
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")

# Загрузка изображений
background = pygame.image.load(os.path.join(os.path.dirname(__file__), "background.jpg"))
ship_image = pygame.image.load(os.path.join(os.path.dirname(__file__), "spaceship_3d.png"))  # 3D модель корабля
asteroid_image = pygame.image.load(os.path.join(os.path.dirname(__file__), "asteroid.png"))
explosion_image = pygame.image.load(os.path.join(os.path.dirname(__file__), "explosion.png"))

# Масштабирование изображений
ship_image = pygame.transform.scale(ship_image, (60, 50))
asteroid_image = pygame.transform.scale(asteroid_image, (50, 50))
explosion_image = pygame.transform.scale(explosion_image, (60, 60))

# Цвета
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)

# Игровые переменные
ship_x = WIDTH // 2
ship_y = HEIGHT - 80
ship_speed = 5
bullets = []
asteroids = []
explosions = []
exhaust_particles = []

# Скорость астероидов
asteroid_speed = 2  

# Усиления
fast_shooting = False
slow_motion = False
powerup_timer = 0

# Таймер игры
game_time = 0
clock = pygame.time.Clock()

# Автоматическая стрельба
shooting = False
shoot_delay = 300  # Время между выстрелами (мс)
last_shot = pygame.time.get_ticks()

# Функция для создания комет (астероидов)
def spawn_asteroid():
    x = random.randint(0, WIDTH - 50)
    y = -50
    speed_x = random.choice([-1, 1]) * random.uniform(1, 2)  # Горизонтальное движение
    speed_y = asteroid_speed
    asteroids.append([x, y, speed_x, speed_y])

# Функция для создания выхлопных частиц
def create_exhaust():
    exhaust_particles.append([ship_x + 30, ship_y + 50, random.randint(3, 6)])

# Основной игровой цикл
running = True
while running:
    screen.blit(background, (0, 0))

    # Управление событиями
    keys = pygame.key.get_pressed()
    
    # Движение корабля
    if keys[pygame.K_LEFT] and ship_x > 0:
        ship_x -= ship_speed
    if keys[pygame.K_RIGHT] and ship_x < WIDTH - 60:
        ship_x += ship_speed

    # Усиление: Остановка времени
    if keys[pygame.K_s]:
        slow_motion = True
        powerup_timer = pygame.time.get_ticks() + 3000  # 3 секунды
    if pygame.time.get_ticks() > powerup_timer:
        slow_motion = False

    # Автоматическая стрельба
    if keys[pygame.K_SPACE]:
        shooting = True
    else:
        shooting = False

    # Усиление: Быстрая стрельба
    if keys[pygame.K_f]:
        fast_shooting = True
        shoot_delay = 100  # Быстрая стрельба
        powerup_timer = pygame.time.get_ticks() + 3000  # 3 секунды
    if pygame.time.get_ticks() > powerup_timer:
        fast_shooting = False
        shoot_delay = 300  # Обычная стрельба

    # Стрельба
    if shooting and pygame.time.get_ticks() - last_shot > shoot_delay:
        bullets.append([ship_x + 25, ship_y])
        last_shot = pygame.time.get_ticks()

    # Отрисовка корабля
    screen.blit(ship_image, (ship_x, ship_y))

    # Обновление и отрисовка пуль
    for bullet in bullets[:]:
        bullet[1] -= 7
        if bullet[1] < 0:
            bullets.remove(bullet)
        pygame.draw.rect(screen, BLUE, (bullet[0], bullet[1], 5, 15))

    # Спавн комет
    if random.randint(1, 100) < 2:  # Редкий спавн
        spawn_asteroid()

    # Обновление и отрисовка комет
    for asteroid in asteroids[:]:
        asteroid[0] += asteroid[2]  # Горизонтальное движение
        asteroid[1] += asteroid[3] * (0.3 if slow_motion else 1)  # Медленнее, если остановлено время

        # Рикошет от стен
        if asteroid[0] <= 0 or asteroid[0] >= WIDTH - 50:
            asteroid[2] = -asteroid[2]

        if asteroid[1] > HEIGHT:
            asteroids.remove(asteroid)  # Удаление кометы, если она улетела вниз

        screen.blit(asteroid_image, (asteroid[0], asteroid[1]))

    # Проверка столкновений пуль с кометами
    for bullet in bullets[:]:
            for asteroid in asteroids[:]:
                if asteroid[0] < bullet[0] < asteroid[0] + 50 and asteroid[1] < bullet[1] < asteroid[1] + 50:
                    bullets.remove(bullet)
                    asteroids.remove(asteroid)  # Добавляем взрыв

    # Отрисовка взрывов
    for explosion in explosions[:]:
        if pygame.time.get_ticks() - explosion[2] < 500:  # Взрыв длится 500 мс
            screen.blit(explosion_image, (explosion[0], explosion[1]))
        else:
            explosions.remove(explosion)

    # Выхлоп газа
    create_exhaust()
    for particle in exhaust_particles[:]:
        particle[1] += 2  # Движение вниз
        particle[2] -= 0.1  # Уменьшение размера
        pygame.draw.circle(screen, ORANGE, (particle[0], particle[1]), int(particle[2]))
        if particle[2] <= 0:
            exhaust_particles.remove(particle)

    # Таймер игры
    game_time += clock.get_time()
    timer_text = pygame.font.SysFont("Arial", 24).render(f"Время: {game_time // 1000} сек", True, WHITE)
    screen.blit(timer_text, (10, 10))

    # Обновление экрана
    pygame.display.flip()
    clock.tick(60)  # Ограничение FPS

    # Обработка выхода из игры
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()