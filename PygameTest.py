# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

ship = pygame.image.load("ship.png")
imgSize = (100,50)
ship = pygame.transform.scale(ship, imgSize)

print(screen.get_width()/2 - ship.get_width()/2)
ship_left = screen.get_width()/2 - ship.get_width()
print(screen.get_height()/2- ship.get_height()/2)
ship_top = screen.get_height()/2 - ship.get_height()
ship_rect = ship.get_rect(top=ship_top, left=ship_left)

print(ship_rect)
while running:

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("light blue")
    pygame.draw.circle(screen, "blue", pygame.Vector2(590, 335),30)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        ship_rect.move_ip(0,-600*dt)
    if keys[pygame.K_s]:
        ship_rect.move_ip(0,600*dt)
    if keys[pygame.K_a]:
        ship_rect.move_ip(-600*dt,0)
    if keys[pygame.K_d]:
        ship_rect.move_ip(600*dt,0)

    ship_rect.clamp_ip(screen.get_bounding_rect())

    screen.blit(ship, ship_rect)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()