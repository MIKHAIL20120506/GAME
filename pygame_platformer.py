import pygame

screen = pygame.display.set_mode((500, 500))
x = 0
y = 0
hitbox:pygame.Rect(0,0,0,0)
pressed_key = None
clock = pygame.time.Clock()
speed = 1

objects = []

floor = {
        "width":300,
        "height":20,
        "color":"green",
        "x":0,
        "y":480,
        "hitbox":pygame.Rect(0,0,0,0)
        }
        
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                pressed_key = "right"
            if event.key == pygame.K_LEFT:
                pressed_key = "left"
            if event.key == pygame.K_SPACE:
                pressed_key = "space"
        if event.type == pygame.KEYUP:
            pressed_key = None
    if pressed_key == "right":
        x += 1
    if pressed_key == "left":
        x -= 1
   if pressed_key == "space":
        speed= - 2
    speed+0.01
    if pygame.Rect.colliderect(hitbox, floor["hitbox"]):
    floor["hitbox"] = pygame.Rect(floor["x"], floor['y'], floor['width'], floor['height'])
    hitbox = pygame.Rect(x, y, 50, 50)
    screen.fill("black")
    pygame.draw.rect(screen, floor["color"], (floor["x"], floor["y"], floor["width"], floor['height']))
    pygame.draw.circle(screen, "red", (400, 400), 50)
    pygame.draw.rect(screen, "yellow", (x, y, 50, 50))
    clock.tick(60)
    pygame.display.update()


