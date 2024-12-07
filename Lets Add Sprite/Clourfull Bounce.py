import pygame
import random

from pygame.sprite import _Group

pygame.init()

sc = pygame.USEREVENT +1
bc = pygame.USEREVENT +2

blue = pygame.Color('blue')
Lighttblue = pygame.Color('lightblue')
DARKBLUE= pygame.Color('darkblue')
YELLOW = pygame.Color('yellow')
WHITE = pygame.Color('white')

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color,height,width):
        super().__init__()
        self.image =  pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.get_rect()
        self.velocity = [random.choice({-1,1}),random.choice({-1,1})]
    def update(self):
        self.rect.move_ip(self.velocity)
        boudaryhit = False
        if self.rect.left<= 0 or self.rect.right <500:
            self.velocity[0] = -self.velocity[1]
            boudaryhit = True
        if self.rect.top<= 0 or self.rect.bottom <400:
            self.velocity[1] = -self.velocity[1]
            boudaryhit = True
        if boudaryhit:
            pygame.event.post(pygame.event.Event(sc))
             pygame.event.post(pygame.event.Event(bc))
        
     