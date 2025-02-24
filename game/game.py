# import pygame
# import random

# # Инициализация Pygame
# pygame.init()

# # Настройки окна
# WIDTH, HEIGHT = 500, 600
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Мини-шутер")

# # Цвета
# WHITE = (255, 255, 255)
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)
# BLUE = (0, 0, 255)
# BLACK = (0, 0, 0)

# # Шрифт
# font = pygame.font.Font(None, 36)

# # Класс игрока
# class Player:
#     def __init__(self):
#         self.width = 50
#         self.height = 50
#         self.x = WIDTH // 2 - self.width // 2
#         self.y = HEIGHT - self.height - 10
#         self.speed = 5

#     def move(self, keys):
#         if keys[pygame.K_LEFT] and self.x > 0:
#             self.x -= self.speed
#         if keys[pygame.K_RIGHT] and self.x < WIDTH - self.width:
#             self.x += self.speed

#     def draw(self):
#         pygame.draw.rect(screen, BLUE, (self.x, self.y, self.width, self.height))

# # Класс пули
# class Bullet:
#     def __init__(self, x, y):
#         self.x = x + 20
#         self.y = y
#         self.speed = 7
#         self.width = 10
#         self.height = 20

#     def move(self):
#         self.y -= self.speed

#     def draw(self):
#         pygame.draw.rect(screen, GREEN, (self.x, self.y, self.width, self.height))

# # Класс врага
# class Enemy:
#     def __init__(self):
#         self.width = 50
#         self.height = 50
#         self.x = random.randint(0, WIDTH - self.width)
#         self.y = -self.height
#         self.speed = 3

#     def move(self):
#         self.y += self.speed

#     def draw(self):
#         pygame.draw.rect(screen, RED, (self.x, self.y, self.width, self.height))

# # Основной игровой цикл
# player = Player()
# bullets = []
# enemies = []
# kills = 0
# running = True
# clock = pygame.time.Clock()

# while running:
#     screen.fill(WHITE)
#     keys = pygame.key.get_pressed()

#     # Движение игрока
#     player.move(keys)
#     player.draw()

#     # Отрисовка счетчика килов
#     score_text = font.render(f"Kills: {kills}", True, BLACK)
#     screen.blit(score_text, (10, 10))

#     # Движение и отрисовка пуль
#     for bullet in bullets[:]:
#         bullet.move()
#         if bullet.y < 0:
#             bullets.remove(bullet)
#         bullet.draw()

#     # Генерация врагов
#     if random.randint(1, 40) == 1:
#         enemies.append(Enemy())

#     # Движение и отрисовка врагов
#     for enemy in enemies[:]:
#         enemy.move()
#         if enemy.y > HEIGHT:
#             print("Вы пропустили врага! Игра окончена!")
#             running = False  # Конец игры, если враг дошел до низа экрана

#         enemy.draw()

#         # Проверка столкновения с игроком
#         if player.x < enemy.x + enemy.width and player.x + player.width > enemy.x and player.y < enemy.y + enemy.height and player.y + player.height > enemy.y:
#             print("Игра окончена! Враг вас задел!")
#             running = False

#         # Проверка попадания пули
#         for bullet in bullets[:]:
#             if bullet.x < enemy.x + enemy.width and bullet.x + bullet.width > enemy.x and bullet.y < enemy.y + enemy.height and bullet.y + bullet.height > enemy.y:
#                 enemies.remove(enemy)
#                 bullets.remove(bullet)
#                 kills += 1  # Увеличиваем счетчик убийств

#     # Стрельба
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_SPACE:
#                 bullets.append(Bullet(player.x, player.y))

#     pygame.display.flip()
#     clock.tick(60)

# print(f"Игра окончена! Ваш счет: {kills}")
# pygame.quit() 






import pygame
import random

# Инициализация Pygame
pygame.init()

# Настройки окна
WIDTH, HEIGHT = 500, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Космический шутер")

# Загрузка изображений
player_img = pygame.image.load("spaceship.png")  # Космолет
player_img = pygame.transform.scale(player_img, (50, 50))  # Изменение размера
background = pygame.image.load(r"C:\Users\Arsen\PycharmProjects\second_month\game\background.jpg")  # Фон  
enemy_img = pygame.image.load("asteroid.png")  # Комета
enemy_img = pygame.transform.scale(enemy_img, (50, 50))  # Изменение размера

# Цвета
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Шрифт
font = pygame.font.Font(None, 36)

# Класс игрока
class Player:
    def __init__(self):
        self.width = 50
        self.height = 50
        self.x = WIDTH // 2 - self.width // 2
        self.y = HEIGHT - self.height - 10
        self.speed = 5

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < WIDTH - self.width:
            self.x += self.speed

    def draw(self):
        screen.blit(player_img, (self.x, self.y))

# Класс пули
class Bullet:
    def __init__(self, x, y):
        self.x = x + 20
        self.y = y
        self.speed = 7
        self.width = 10
        self.height = 20

    def move(self):
        self.y -= self.speed

    def draw(self):
        pygame.draw.rect(screen, GREEN, (self.x, self.y, self.width, self.height))

# Класс врага (кометы)
class Enemy:
    def __init__(self):
        self.width = 50
        self.height = 50
        self.x = random.randint(0, WIDTH - self.width)
        self.y = -self.height
        self.speed = 3

    def move(self):
        self.y += self.speed

    def draw(self):
        screen.blit(enemy_img, (self.x, self.y))

# Основной игровой цикл
player = Player()
bullets = []
enemies = []
kills = 0
running = True
clock = pygame.time.Clock()

while running:
    screen.blit(background, (0, 0))  # Отрисовка фона
    keys = pygame.key.get_pressed()

    # Движение игрока
    player.move(keys)
    player.draw()

    # Отрисовка счетчика килов
    score_text = font.render(f"Kills: {kills}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Движение и отрисовка пуль
    for bullet in bullets[:]:
        bullet.move()
        if bullet.y < 0:
            bullets.remove(bullet)
        bullet.draw()

    # Генерация комет
    if random.randint(1, 40) == 1:
        enemies.append(Enemy())

    # Движение и отрисовка комет
    for enemy in enemies[:]:
        enemy.move()
        if enemy.y > HEIGHT:
            print("Вы пропустили комету! Игра окончена!")
            running = False  # Конец игры, если комета дошла до низа экрана

        enemy.draw()

    # Проверка столкновения с игроком
        if player.x < enemy.x + enemy.width and player.x + player.width > enemy.x and player.y < enemy.y + enemy.height and player.y + player.height > enemy.y:
            print("Игра окончена! Комета врезалась в вас!")
            running = False

        # Проверка попадания пули
        for bullet in bullets[:]:
            if bullet.x < enemy.x + enemy.width and bullet.x + bullet.width > enemy.x and bullet.y < enemy.y + enemy.height and bullet.y + bullet.height > enemy.y:
                if enemy in enemies:
                    enemies.remove(enemy)
                if bullet in bullets:
                    bullets.remove(bullet)
                kills += 1  # Увеличиваем счетчик убийств

    # Стрельба
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append(Bullet(player.x, player.y))

    pygame.display.flip()
    clock.tick(60)

print(f"Игра окончена! Ваш счет: {kills}")
pygame.quit()
