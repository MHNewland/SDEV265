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
        if(initial):
            self.rect = self.image.get_rect()
        else:
            self.rect = self.image.get_rect(left=self.screen.get_bounding_rect().right + self.image.get_width()/2)

        self.spawned_next = False


    def move_background(self, dt):
        self.rect.move_ip(-self.speed*dt,0)
        if(not self.spawned_next and
           self.rect.left <= self.screen.get_bounding_rect().right):
            self.spawned_next = True
            return True
        
        if (self.rect.right < 0):
            self.kill()
