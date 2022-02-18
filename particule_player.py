import pygame as pg

image_part = {"quark up" : ['asset/testparticule.png', 400, 250] , "quark down" : ['asset/testpart.jpeg', 700,250], "quark bottom" : ['asset/quarkb.jpeg', 700,450]}
class Player1(pg.sprite.Sprite):
    def __init__(self, particule1):
        super().__init__()#to call the class init
        self.image = pg.image.load(image_part[particule1][0])
        self.image = pg.transform.scale(self.image, (55, 55))
        self.rect = self.image.get_rect()#deplacement
        self.rect.x = image_part[particule1][1] #position init
        self.rect.y = image_part[particule1][2]

class Player2(pg.sprite.Sprite):
    def __init__(self, particule2):
        super().__init__()#to call the class init
        self.image = pg.image.load(image_part[particule2][0])
        self.image = pg.transform.scale(self.image, (55, 55))
        self.rect = self.image.get_rect()#deplacement
        self.rect.x = image_part[particule2][1] #position init
        self.rect.y = image_part[particule2][2]

class Player3(pg.sprite.Sprite):
    def __init__(self, particule3):
        super().__init__()#to call the class init
        self.image = pg.image.load(image_part[particule3][0])
        self.image = pg.transform.scale(self.image, (55, 55))
        self.rect = self.image.get_rect()#deplacement
        self.rect.x = image_part[particule3][1] #position init
        self.rect.y = image_part[particule3][2]
