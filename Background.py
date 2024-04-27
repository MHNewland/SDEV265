import pygame

class Background(pygame.sprite.Sprite):
    #pygame.sprite variables
    image: pygame.surface
    rect: pygame.rect

    img_str: str
    screen: pygame.surface
    speed: int
    position: pygame.Vector2
    spawned_next: bool

    def __init__(self, screen, img_str: str, speed: int, *initial: bool):
        super().__init__()
        self.screen = screen
        self.img_str = img_str
        self.image = pygame.image.load(img_str).convert_alpha()
        self.speed = speed
        #if it's the initial spawn of the backgrounds, put them in the middle of the screen
        if(initial):
            self.rect = self.image.get_rect()
        else:
            #otherwise, set the background to spawn outside the screen to the right
            self.rect = self.image.get_rect(left=self.screen.get_bounding_rect().right + self.image.get_width()/2)

        self.spawned_next = False


    def move_background(self, dt, difficulty):
        """
        moves the background to the left based on the speed when it was created
        if it hasn't spawned the next background to loop and the left of the background
            has passed the right side of the screen, spawn the next background.
        Once the right side of the background image passes the left side of the screen,
            destroy the image.
        """
        self.rect.move_ip(-(self.speed+difficulty)*dt,0)
        if(not self.spawned_next and
           self.rect.left <= self.screen.get_bounding_rect().right):
            self.spawned_next = True
            return True
        
        if (self.rect.right < 0):
            self.kill()
