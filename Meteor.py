import pygame
import random
import math

class Meteor(pygame.sprite.Sprite):

    meteor_pos: pygame.Vector2
    screen: pygame.surface
    speed: int

    def __init__(self, screen:pygame.surface):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load("meteor.png")
        imgWidth = random.randint(50,100)
        imgHeight = random.randint(50,100)
        imgSize = (imgWidth, imgHeight)
        self.image = pygame.transform.scale(self.image, imgSize)
        self.mask = pygame.mask.from_surface(self.image.convert_alpha())

        meteor_posX = self.screen.get_bounding_rect().right + imgWidth/2
        yMin = imgHeight/2
        yMax = self.screen.get_bounding_rect().bottom - imgHeight/2
        meteor_posY = random.randint(math.floor(yMin), math.floor(yMax))
        self.meteor_pos = pygame.Vector2(meteor_posX, meteor_posY)
        self.speed = random.randint(100,600)

        self.rect = self.image.get_rect(top=meteor_posY-imgHeight/2, left=meteor_posX-imgWidth/2)

    def move_meteor(self, dt):
        self.rect.move_ip(-self.speed*dt,0)
        if (self.rect.left < 0-self.rect.width/2):
            self.kill()
            return True
    
