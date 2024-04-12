import pygame
import Player
import Meteor
import ScoreManager
import Background

# pygame setup
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

background_array = pygame.sprite.Group()
background_near = Background.Background(screen, "background_near.png", 300, True)
background_med = Background.Background(screen, "background_med.png", 200, True)
background_far = Background.Background(screen, "background_far.png", 100, True)
background_array.add([background_near, background_med, background_far])
score_manager = ScoreManager.ScoreManager(screen)

meteor_spawn_delay = 2
meteor_timer = 0
meteor_array = pygame.sprite.Group()

player_sprite = pygame.sprite.GroupSingle()
ship = Player.Player(screen)
player_sprite.add(ship)

while running:
    meteor_timer+=dt
    if(meteor_timer>=meteor_spawn_delay):
        meteor_timer=0
        meteor_array.add(Meteor.Meteor(screen))

    for m in meteor_array:
        if(m.move_meteor(dt)):
            score_manager.current_score +=1
    
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    for b in background_array.sprites():
        if(b.move_background(dt)):
            background_array.add(Background.Background(screen, b.img_str, b.speed))
    background_array.draw(screen)
    player_sprite.sprite.move_ship(dt)

    meteor_array.draw(screen)
    player_sprite.draw(screen)
    score_text, score_pos = score_manager.draw()
    screen.blit(score_text, score_pos)


    for m in meteor_array.sprites():
        if(not player_sprite.sprite.invulnerable):
            if pygame.sprite.spritecollide(m, player_sprite, False, pygame.sprite.collide_mask):
                if(player_sprite.sprite.hit()):
                    running = False
        else:    
            player_sprite.sprite.check_invulnerable(dt)
        

                
    
    

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 30
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(30) / 1000

pygame.time.wait(1000)

pygame.quit()
