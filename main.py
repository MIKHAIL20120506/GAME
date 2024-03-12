import pygame # Строка для включения в проект функции из библеотеки pygame
screen_heigh = 600
screen_width = 600
screen = pygame.display.set_mode((screen_width, screen_heigh))
game_size = 10
box_size = screen_width/game_size
game = {} # игровой словарь, хранящий в себе информацию
snake_look = "right"
snake_pos = "3_3"

def create_field_dict():
    global snake_pos
    y_count = 0
    while y_count < game_size:
        x_count = 0
        while x_count < 10:
            game[str(x_count)+"_"+str(y_count)]= "empty"
            x_count += 1
        y_count += 1
    game["2_2"] = "snake"
    snake_pos = "3_3"
    
    
def draw_objects():
    y_count = 0
    while y_count < game_size:
        x_count = 0
        while x_count < game_size:
           current_obj = game[str(x_count)+"_"+str(y_count)]
           if current_obj == "snake":
            pygame.draw.rect(screen, "green", (x_count*box_size, y_count*box_size, box_size, box_size))
           x_count += 1
        y_count += 1
        

    
def draw_field():
    y_count = 0
    while y_count < game_size:
        x_count = 0
        while x_count < 10:
            pygame.draw.rect(screen, "green", (x_count*box_size, y_count*box_size, box_size, box_size),1)
            x_count += 1
        y_count += 1

def move_snake():
    global snake_pos
    x = int(snake_pos.split("_") [0])
    y = int(snake_pos.split("_") [1])
    if snake_look  == "right":
        x += 1
    if snake_look  == "left":
        x -= 1
    if snake_look  == "up":
        x -= 1
    if snake_look  == "down":
        x += 1
    new_coords = str(x)+ "_"+str(y)
    game[new_coords] = "snake"
    snake_pos = new_coords
    

       
create_field_dict()
iter_count = 0
while True: # бесконечный  игровой цикл
    iter_count += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    screen.fill("black")
    draw_field()
    if iter_count % 60 == 0:
        move_snake()
    draw_objects()
    pygame.display.update()

    


    
