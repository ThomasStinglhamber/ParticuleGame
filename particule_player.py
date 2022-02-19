import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, particule1, color, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([40,40], pygame.SRCALPHA)
        self.rect = self.image.get_rect()#deplacement
        self.rect.x = x
        self.rect.y = y
        pygame.draw.circle(self.image, color, (20, 20),20, 0)
