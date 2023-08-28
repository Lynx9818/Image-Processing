import pygame

pygame.init()

screen = pygame.display.set_mode((500, 600))

GREY = (150, 150, 150)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

running = True

while running:
    screen.fill(GREY)

    pygame.draw.rect(screen, WHITE, (100, 50, 50, 50))
    pygame.draw.rect(screen, WHITE, (200, 50, 50, 50))
    pygame.draw.rect(screen, RED, (300, 50, 100, 50))
    pygame.draw.rect(screen, WHITE, (100, 200, 50, 50))
    pygame.draw.rect(screen, WHITE, (200, 200, 50, 50))
    pygame.draw.rect(screen, RED, (300, 200, 100, 50))

    pygame.draw.circle(screen, BLACK, (250, 375), 100)
    pygame.draw.circle(screen, WHITE, (250, 375), 95)
    pygame.draw.circle(screen, BLACK, (250, 375), 5)
    
    pygame.draw.rect(screen, BLACK, (50,500,400,50))
    pygame.draw.rect(screen, WHITE, (55,505,390,40))

    pygame.draw.line(screen, BLACK, (250, 375), (250, 285))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print("XXX")

    pygame.display.flip()

pygame.quit()
