import pygame
import random


# Ініціалізація Pygame
pygame.init()

# Налаштування вікна
WIDTH, HEIGHT = 600, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Рандомайзер малюнків 1-28")

# Кольори
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (50, 150, 255)

# Шрифти
font_main = pygame.font.SysFont("Arial", 24)
font_button = pygame.font.SysFont("Arial", 30, bold=True)

# Глобальні змінні
current_image = None
current_number = "?"
button_rect = pygame.Rect(WIDTH // 2 - 100, 550, 200, 60)

def load_random_image():
    """Обирає випадкове число та завантажує відповідний малюнок"""
    num = random.randint(1, 28)
    path = f"{num}.png"

    img = pygame.image.load(path)
    # Масштабуємо малюнок, щоб він вписався у вікно (наприклад, 400x400)
    img = pygame.transform.scale(img, (400, 400))
    return img, num
  

# Головний цикл програми
running = True
while running:
    screen.fill(WHITE)
    
    # Обробка подій
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Перевірка натискання мишки
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                current_image, current_number = load_random_image()
        
        # Перевірка натискання клавіші Пропуск (Space)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                current_image, current_number = load_random_image()

    # --- Малюємо інтерфейс ---

    # Текст зверху
    text_top = font_main.render(f"Вибрано номер: {current_number}", True, BLACK)
    screen.blit(text_top, (WIDTH // 2 - text_top.get_width() // 2, 30))

    # Рамка для малюнка
    pygame.draw.rect(screen, GRAY, (WIDTH // 2 - 205, 100 - 5, 410, 410), 2)

    # Вивід малюнка
    if current_image:
        screen.blit(current_image, (WIDTH // 2 - 200, 100))
    else:
        # Якщо малюнка немає, пишемо текст у центрі рамки
        placeholder = font_main.render("Тут буде малюнок", True, GRAY)
        screen.blit(placeholder, (WIDTH // 2 - placeholder.get_width() // 2, 280))

    # Малюємо кнопку
    mouse_pos = pygame.mouse.get_pos()

    pygame.draw.rect(screen,BLUE, button_rect, border_radius=10)
    
    text_btn = font_button.render("PUSH", True, WHITE)
    screen.blit(text_btn, (button_rect.centerx - text_btn.get_width() // 2, 
                           button_rect.centery - text_btn.get_height() // 2))

    # Підказка знизу
    hint = font_main.render("Натисніть кнопку або SPACE", True, GRAY)
    screen.blit(hint, (WIDTH // 2 - hint.get_width() // 2, 630))

    # Оновлення екрана
    pygame.display.flip()

pygame.quit()