import pygame

class Player(pygame.sprite.Sprite):
    #pygame.sprite variables
    image: pygame.surface
    rect:pygame.rect

    screen: pygame.surface
    position: pygame.Vector2
    ship_images: list
    index: int
    ship_anim_speed: float
    ship_anim_timer: float
    ship_alpha: pygame.surface
    blank_img: pygame.surface
    mask: pygame.mask

    invulnerable: bool
    invulnerable_time: int
    invulnerable_timer:float
    
    blink_image: bool
    blink_timer: int
    blink_speed: float

    speed: int
    lives:int

    def __init__(self, screen:pygame.surface):
        super().__init__()
        self.screen = screen
        #set ship to middle of screen.
        self.position = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

        imgSize = (110,55)

        #load all ship animation images
        self.index = 0
        self.ship_images = []
        self.ship_images.append(pygame.transform.scale(pygame.image.load("ship1.png"), imgSize))
        self.ship_images.append(pygame.transform.scale(pygame.image.load("ship2.png"), imgSize))
        self.ship_images.append(pygame.transform.scale(pygame.image.load("ship3.png"), imgSize))
        self.ship_anim_speed = 10
        self.ship_anim_timer = 0

        #load blank image for flashing ship and the ship alpha for collision.
        self.blank_img = pygame.image.load("blank.png")
        self.ship_alpha = pygame.image.load("ShipAlpha.png")        

        #set all images to the correct size.
        self.ship_alpha = pygame.transform.scale(self.ship_alpha, imgSize)
    
        #set start image
        self.image = self.ship_images[0]

        #create mask from the alpha
        self.mask = pygame.mask.from_surface(self.ship_alpha.convert_alpha())

        #place ship in middle of screen.
        ship_left = screen.get_width()/2 - self.image.get_width()
        ship_top = screen.get_height()/2 - self.image.get_height()
        self.rect = self.image.get_rect(top=ship_top, left=ship_left)

        self.invulnerable = False
        self.invulnerable_time = 3
        self.invulnerable_timer = 0

        self.blink_image = False
        self.blink_timer = 0
        self.blink_speed = 4

        self.lives=0
        self.speed = 600
    

    def move_ship(self, dt):
        """
        Moves the ship Up, Left, Down, or Right
        based on key presses of W, A, S, and D respectively,
        and clamps the rect to the screen.
        returns null if deltaTime(dt) is not an int or float.
        """
        #if dt isn't an int or float, error
        if(not (isinstance(dt, int) or isinstance(dt, float))):
            return
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.rect.move_ip(0,-self.speed*dt)
        if keys[pygame.K_s]:
            self.rect.move_ip(0,self.speed*dt)
        if keys[pygame.K_a]:
            self.rect.move_ip(-self.speed*dt,0)
        if keys[pygame.K_d]:
            self.rect.move_ip(self.speed*dt,0)

        self.rect.clamp_ip(self.screen.get_bounding_rect())

    def check_invulnerable(self, dt):
        """
        Checks to see if the ship is still 
        invulnerable after being hit.

        while the ship is invulnerable, it blinks the image
        equal to the blink_speed per second.
        """
        self.invulnerable_timer += dt
        self.blink_timer += dt

        if( self.invulnerable_timer >= self.invulnerable_time):
            self.invulnerable_timer = 0
            self.invulnerable = False
            self.image = self.ship_images[0]
        else:
            if(self.blink_timer >= 1/(self.blink_speed*2)):
                self.flip_img()
                self.blink_timer = 0

    def flip_img(self):
        """
        swaps the ship image with a blank image
        to give a blinking effect.
        """
        self.blink_image = not self.blink_image
        if(self.blink_image):
            self.image = self.blank_img
        else:
            self.image = self.image
        

    def hit(self):
        """
        if the player didn't have any more lives, returns true
        otherwise, it sets invulnerable to true and subtracts
        one from lives
        """
        if(self.lives == 0):
            return True
        self.invulnerable = True
        self.lives -=1


    def update(self, dt):
        """
        handles ship animation
        """

        if(not (isinstance(dt, int) or isinstance(dt, float))):
            return
        
        self.ship_anim_timer += dt
        if(self.ship_anim_timer >= 1/self.ship_anim_speed):
            self.ship_anim_timer = 0
            self.index += 1
    
            if self.index >= len(self.ship_images):
                self.index = 0
            
            self.image = self.ship_images[self.index]