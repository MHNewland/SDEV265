import pygame
import random
import math

class Meteor(pygame.sprite.Sprite):
    #pygame.sprite variables
    image: pygame.surface
    rect: pygame.rect

    #position: pygame.Vector2
    screen: pygame.surface
    speed: int
    mask: pygame.mask

    def __init__(self, screen:pygame.surface, difficulty: int):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load("Images/meteor.png").convert_alpha()
        imgWidth = random.randint(50,100)
        imgHeight = random.randint(50,100)
        imgSize = (imgWidth, imgHeight)
        self.image = pygame.transform.scale(self.image, imgSize)
        self.mask = pygame.mask.from_surface(self.image.convert_alpha())

        meteor_posX = self.screen.get_bounding_rect().right + imgWidth/2
        yMin = imgHeight/2
        yMax = self.screen.get_bounding_rect().bottom - imgHeight/2
        meteor_posY = random.randint(math.floor(yMin), math.floor(yMax))
        #self.position = pygame.Vector2(meteor_posX, meteor_posY)
        self.speed = random.randint(100+difficulty,600+difficulty)

        self.rect = self.image.get_rect(top=meteor_posY-imgHeight/2, left=meteor_posX-imgWidth/2)

    def move_meteor(self, dt):
        """
        Moves the meteor left
        If the right side of the meteor passes the left side of the screen,
            destroys the meteor and returns True.
        """
        self.rect.move_ip(-self.speed*dt,0)
        if (self.rect.right < 0):
            self.kill()
            return True
    
