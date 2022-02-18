import pygame

class Player1(pygame.sprite.Sprite):
    def __init__(self, particule1, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([40,40], pygame.SRCALPHA)
        self.rect = self.image.get_rect()#deplacement
        self.rect.x = 200
        self.rect.y = 200
        pygame.draw.circle(self.image, color, (20, 20),20, 0)


class Player2(pygame.sprite.Sprite):
    def __init__(self, particule2,color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([40,40], pygame.SRCALPHA)
        self.rect = self.image.get_rect()#deplacement
        self.rect.x = 500
        self.rect.y = 200
        pygame.draw.circle(self.image, color, (20, 20),20, 0)


class Player3(pygame.sprite.Sprite):
    def __init__(self, particule3, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([40,40], pygame.SRCALPHA)
        self.rect = self.image.get_rect()#deplacement
        self.rect.x = 1000
        self.rect.y = 250
        pygame.draw.circle(self.image, color, (20, 20),20, 0)
