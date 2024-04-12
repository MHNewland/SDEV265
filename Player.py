import pygame

class Player(pygame.sprite.Sprite):
    #pygame.sprite variables
    image: pygame.surface
    rect:pygame.rect

    screen: pygame.surface
    position: pygame.Vector2
    ship_image: pygame.surface
    blank_img: pygame.surface
    mask: pygame.mask

    invulnerable: bool
    invulnerable_time: int
    invulnerable_timer:float
    
    blink_image: bool
    blink_timer: int
    blink_speed: float

    lives:int

    def __init__(self, screen:pygame.surface):
        super().__init__()
        self.screen = screen
        self.position = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
        self.ship_image = pygame.image.load("ship.png").convert_alpha()
        self.blank_img = pygame.image.load("blank.png")        

        imgSize = (100,50)
        self.image = pygame.transform.scale(self.ship_image, imgSize)
        self.ship_image = self.image.copy()
        self.mask = pygame.mask.from_surface(self.image.convert_alpha())

        ship_left = screen.get_width()/2 - self.image.get_width()
        ship_top = screen.get_height()/2 - self.image.get_height()
        self.rect = self.image.get_rect(top=ship_top, left=ship_left)

        self.invulnerable = False
        self.invulnerable_time = 3
        self.invulnerable_timer = 0

        self.blink_image = False
        self.blink_timer = 0
        self.blink_speed = 1/8

        self.lives=3
    
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
        self.invulnerable_timer += dt
        self.blink_timer += dt

        if( self.invulnerable_timer >= self.invulnerable_time):
            self.invulnerable_timer = 0
            self.invulnerable = False
            self.image = self.ship_image
        else:
            if(self.blink_timer >= self.blink_speed):
                self.flip_img()
                self.blink_timer = 0

    def flip_img(self):
        self.blink_image = not self.blink_image
        if(self.blink_image):
            self.image = self.blank_img
        else:
            self.image = self.ship_image
        

    def hit(self):
        if(self.lives == 0):
            return True
        self.invulnerable = True
        self.lives -=1
        