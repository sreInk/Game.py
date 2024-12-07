import pygame
pygame.init()
screen = pygame.display.set_mode((400,500))
screen.fill((225,225,225))
GREEN = (0,225,0)
pygame.draw.circle(screen,GREEN,(100,300),50)
pygame.draw.circle(screen,GREEN,(050,060),50,3)
pygame.display.update()
done = True
while done:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = False
                pygame.quit()
