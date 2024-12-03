import pygame
pygame.init()
white = (225,225,225)
clock = pygame.time.Clock()
displaysurface = pygame.display.set_mode((500,500))
pygame.display.set_caption("Image")
image = pygame.image.load("black-myth-wukong-HD-scaled.jpg")
imgsixe = (150,150)
image = pygame.transform.scale(image,imgsixe)
while True:
    displaysurface.fill(white)
    displaysurface.blit(image,imgsixe)
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
    pygame.display.flip()
    clock.tick(30)