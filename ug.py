import pygame
import random

pygame.init()

width = 600
height = 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ufo Game")

black = (0, 0, 0)
white = (255, 255, 255)

distance = 5
fps = 60
score = 0
clock = pygame.time.Clock()

ufo_image = pygame.image.load("Ufo-game/img/ufo.png")
ufo_image_rect = ufo_image.get_rect()
ufo_image_rect.center = (width // 2, height // 2)

earth_image = pygame.image.load("Ufo-game/img/earth.png")
earth_image_rect = earth_image.get_rect()
earth_image_rect.center = (50, height // 2)

font = pygame.font.Font(None, 36)

lets_continue = True

while lets_continue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lets_continue = False

    keys = pygame.key.get_pressed()
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and ufo_image_rect.top > 50 > 0:
        ufo_image_rect.y -= distance
    elif (keys[pygame.K_DOWN] or keys[pygame.K_s]) and ufo_image_rect.bottom < height:
        ufo_image_rect.y += distance
    elif (keys[pygame.K_LEFT] or keys[pygame.K_a]) and ufo_image_rect.left > 0:
        ufo_image_rect.x -= distance
    elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and ufo_image_rect.right < width:
        ufo_image_rect.x += distance

    if ufo_image_rect.colliderect(earth_image_rect):
        earth_image_rect.centerx = random.randint(0 + 16, width - 16)
        earth_image_rect.centery = random.randint(50 + 16, height - 16)
        score += 1


    screen.fill(white)
    screen.blit(ufo_image, ufo_image_rect)
    screen.blit(earth_image, earth_image_rect)

    text_surface = font.render("UFO Game", True, black, white)  
    text_rect = text_surface.get_rect(center=(width // 2, 20))
    screen.blit(text_surface, text_rect)

    score_text = font.render(f"Score: {score}", True, black)
    score_text_rect = score_text.get_rect()
    score_text_rect.x = 10
    score_text_rect.y = 10
    screen.blit(score_text, score_text_rect)



    pygame.display.update()
    clock.tick(fps)

pygame.quit()
