import pygame # Строка для включения в проект функции из библеотеки pygame
screen_heigh = 600
screen_width = 600
screen = pygame.display.set_mode((screen_width, screen_heigh))
game_size = 10

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    pygame.draw.rect(screen, "green", (100,100,50,50))
    pygame.display.update()