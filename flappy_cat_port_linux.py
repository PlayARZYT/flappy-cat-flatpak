import pygame
import random
import os
import sys

pygame.init()
pygame.mixer.init() # Инициализируем звук для Linux/Raspberry Pi

# Настройка путей к файлам внутри Flatpak-пакета
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
def get_path(filename):
    return os.path.join(BASE_DIR, filename)

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

pygame.display.set_caption("Flappy Cat v.1.0 Beta Build") 

# Загружаем иконку
try:
    icon = pygame.image.load(get_path("cat.png"))
    pygame.display.set_icon(icon)
except:
    pass

pygame.display.set_mode((800, 600), pygame.RESIZABLE) 
pygame.display.set_mode((800, 600), pygame.RESIZABLE | pygame.SCALED) 

obstacle_timer = 0 
obstacles = [] 
obstacle_width = 50 
gap_height = 150 
min_distance = 250 

GREY = (125, 125, 125)
GREEN = (0, 163, 108)

# Загрузка кота
cat_img = pygame.image.load(get_path("cat.png")) 
cat_img = pygame.transform.smoothscale(cat_img, (50, 50)) 
cat = cat_img.get_rect() 
cat.topleft = (100, 100) 

font = pygame.font.SysFont("Arial", 24) 
fps_counter = font 
version_label = font.render("v1.0 Beta Build", True, GREY) 

# Загрузка фона
background_img = pygame.image.load(get_path("background.png")) 
background_img = pygame.transform.scale(background_img, (800, 600)) 

# Загрузка звуков через Pygame (замена winsound)
try:
    jump_sound = pygame.mixer.Sound(get_path("jump.wav"))
    crash_sound = pygame.mixer.Sound(get_path("catcrash.wav"))
except:
    jump_sound = None
    crash_sound = None

speed = 0 
gravity = 0.5 
jump_speed = -8 

# --- ОСНОВНОЙ ЦИКЛ ---
while True:
    screen.blit(background_img, (0, 0))  
    screen.blit(fps_counter.render(f"FPS: {int(clock.get_fps())}", True, GREY), (10, 10))  
    screen.blit(version_label, (650, 10))  
    cat_coordinates_label = font.render(f"Cat Coordinates: {cat.topleft}", True, GREY)  
    screen.blit(cat_coordinates_label, (10, 40))  
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            speed = jump_speed  
            if jump_sound:
                jump_sound.play()

    speed += gravity  
    cat.y += speed  

    if cat.y > 550:
        cat.y = 550  
        speed = 0  
    elif cat.y < 0:
        cat.y = 0  
        speed = 0  

    obstacle_timer += 1

    # ВТОРАЯ ЧАСТЬ (Логика препятствий)
    if obstacle_timer > min_distance:
        min_distance = random.randint(100, 300) 
        top_obstacle_height = random.randint(100, 350) 
        bottom_obstacle_height = screen.get_height() - top_obstacle_height - gap_height 

        top_obstacle = pygame.Rect(800, 0, obstacle_width, top_obstacle_height)
        bottom_obstacle = pygame.Rect(800, screen.get_height() - bottom_obstacle_height, obstacle_width, bottom_obstacle_height)

        obstacles.append((top_obstacle, bottom_obstacle))
        obstacle_timer = 0

    for top_obstacle, bottom_obstacle in obstacles:
        top_obstacle.x -= 5 
        bottom_obstacle.x -= 5 

        # Перевірка на зіткнення
        if cat.colliderect(top_obstacle) or cat.colliderect(bottom_obstacle):
            print("Game Over!")
            if crash_sound:
                crash_sound.play()
            
            try:
                cat_img = pygame.image.load(get_path("sadcat.png"))  
                cat_img = pygame.transform.smoothscale(cat_img, (50, 50))
            except:
                pass

            for draw_top, draw_bottom in obstacles:
                pygame.draw.rect(screen, GREEN, draw_top)
                pygame.draw.rect(screen, GREEN, draw_bottom)

            screen.blit(cat_img, cat.topleft)
            pygame.display.update()
            pygame.time.delay(4000)  
            pygame.quit()
            sys.exit()

        if top_obstacle.x < -obstacle_width: 
            obstacles.remove((top_obstacle, bottom_obstacle))

    for top_obstacle, bottom_obstacle in obstacles:
        pygame.draw.rect(screen, GREEN, top_obstacle) 
        pygame.draw.rect(screen, GREEN, bottom_obstacle) 

    screen.blit(cat_img, cat.topleft)
    pygame.display.update()
    clock.tick(60)
