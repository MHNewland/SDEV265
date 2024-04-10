import pygame
import Player
import Meteor
import array

# pygame setup
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

score = 0

meteor_spawn_delay = 2
meteor_timer = 0

meteor_array = pygame.sprite.Group(Meteor.Meteor(screen))

player_sprite = pygame.sprite.GroupSingle(Player.Player(screen))
ship = Player.Player(screen)
player_sprite.add(ship)

score_font = pygame.font.Font(size= 30)


while running:
    meteor_timer+=dt
    if(meteor_timer>=meteor_spawn_delay):
        meteor_timer=0
        meteor_array.add(Meteor.Meteor(screen))

    for m in meteor_array:
        if(m.move_meteor(dt)):
            score +=1
    
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("light blue")
    player_sprite.sprite.move_ship(dt)

    score_text = score_font.render( f"Score: {score}",False, (0,0,0))
    score_posX = screen.get_bounding_rect().right - score_text.get_width() - 20

    meteor_array.draw(screen)
    player_sprite.draw(screen)
    screen.blit(score_text, (score_posX,20))


    for m in meteor_array.sprites():
        player_sprite.sprite.check_invulnerable(dt)
        if pygame.sprite.spritecollide(m, player_sprite, False, pygame.sprite.collide_mask):
            if(not (player_sprite.sprite.invulnerable)):
                print("hit")
                player_sprite.sprite.invulnerable = True

                
    
    

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
