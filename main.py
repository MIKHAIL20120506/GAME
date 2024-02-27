import pygame # Строка для включения в проект функции из библеотеки pygame
screen_heigh = 600
screen_width = 600
screen = pygame.display.set_mode((screen_width, screen_heigh))
game_size = 10
box_size = screen_width/game_size

def draw_field():
    y_count = 0
    while y_count < game_size:
        x_count = 0
        while x_count < 10:
            pygame.draw.rect(screen, "green", (x_count*box_size, y_count*box_size, box_size, box_size),1)
            x_count += 1
        y_count += 1

    

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    screen.fill("black")
    draw_field()
    pygame.display.update()
