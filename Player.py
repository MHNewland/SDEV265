import pygame
import math

class Player(pygame.sprite.Sprite):

    player_pos: pygame.Vector2
    screen: pygame.surface
    invulnerable = False
    invulnerable_time = 3
    timer = 0
    blank_img = pygame.surface
    ship_image = pygame.surface
    flip_image = True
    flip_timer = 0
    flip_speed = 1/4

    def __init__(self, screen:pygame.surface):
        super().__init__()
        self.screen = screen
        self.player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

        self.ship_image = pygame.image.load("ship.png")
        self.blank_img = pygame.image.load("blank.png")
        imgSize = (100,50)
        self.image = pygame.transform.scale(self.ship_image, imgSize)
        self.ship_image = self.image.copy()
        self.mask = pygame.mask.from_surface(self.image.convert_alpha())

        ship_left = screen.get_width()/2 - self.image.get_width()
        ship_top = screen.get_height()/2 - self.image.get_height()
        self.rect = self.image.get_rect(top=ship_top, left=ship_left)
        self.timer = 0

    def move_ship(self, dt):
        #if dt isn't an int or float, error
        if(not (isinstance(dt, int) or isinstance(dt, float))):
            return
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.rect.move_ip(0,-600*dt)
        if keys[pygame.K_s]:
            self.rect.move_ip(0,600*dt)
        if keys[pygame.K_a]:
            self.rect.move_ip(-600*dt,0)
        if keys[pygame.K_d]:
            self.rect.move_ip(600*dt,0)

        self.rect.clamp_ip(self.screen.get_bounding_rect())
        #return self.rect

    def check_invulnerable(self, dt):
        if(not self.invulnerable):
            return
        
        self.timer += dt
        self.flip_timer += dt

        if( self.timer >= self.invulnerable_time):
            self.timer = 0
            self.invulnerable = False
            self.image = self.ship_image
        else:
            if(self.flip_timer >= self.flip_speed):
                print(self.flip_timer)
                self.flip_img()
                self.flip_timer = 0

    def flip_img(self):
        self.flip_image = not self.flip_image
        if(self.flip_image):
            print("blank")
            self.image = self.blank_img
        else:
            self.image = self.ship_image
            print("ship")
        

    