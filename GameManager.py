import pygame
import Player
import Meteor
import ScoreManager
import Background

def StartGame():#return_menu):
    """
    Starts the main game loop.
    return_menu is the screen it'll go to once the game is over.
    """
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    dt = 0

    background_array = pygame.sprite.Group()
    background_near = Background.Background(screen, "Images/background_near.png", 300, True)
    background_med = Background.Background(screen, "Images/background_med.png", 200, True)
    background_far = Background.Background(screen, "Images/background_far.png", 100, True)
    background_array.add([background_near, background_med, background_far])
    score_manager = ScoreManager.ScoreManager(screen)

    meteor_spawn_delay = 2
    meteor_timer = 0
    meteor_array = pygame.sprite.Group()

    player_sprite = pygame.sprite.GroupSingle()
    ship = Player.Player(screen)
    player_sprite.add(ship)    

    difficulty_delay = 2
    difficulty_timer = 0
    difficulty_value = 0

    while running:
        meteor_timer+=dt
        difficulty_timer += dt

        if(difficulty_timer>= difficulty_delay):
            difficulty_timer=0
            difficulty_value+=10

        #Check if it's time to spawn another meteor
        #gets faster, maxing out at a meteor every .25 seconds
        spawn_meteor = max((meteor_spawn_delay - difficulty_value/100 ), 0.25)
        if(meteor_timer >= spawn_meteor):
            meteor_timer=0
            meteor_array.add(Meteor.Meteor(screen, difficulty_value))
        #move all meteors and if they hit the left side, add one to the score
        #not adding the difficulty value to the meteors as we don't want them to 
        #   speed up after spawning.
        for m in meteor_array:
            if(m.move_meteor(dt)):
                score_manager.current_score +=1
        
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.stop()           # Stop all sounds if player clicked the X close button 
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("black")

        #move the background images, if they get fully onto the screen, spawn another
        for b in background_array.sprites():
            if(b.move_background(dt, difficulty_value)):
                background_array.add(Background.Background(screen, b.img_str, b.speed))
        background_array.draw(screen)

        #handle player input
        player_sprite.sprite.move_ship(dt, difficulty_value)

        player_sprite.draw(screen)
        meteor_array.draw(screen)
        score_text, score_pos = score_manager.draw()
        screen.blit(score_text, score_pos)
        for i in range(1,ship.lives+1):
            screen.blit(ship.life_image, (screen.get_bounding_rect().left + ship.life_image.get_width() + 20*i, 20))

        #animate player
        player_sprite.update(dt)

        #if the player is vulnerable, collision check
        if(not player_sprite.sprite.invulnerable):

            #loops through meteors to see if any are hitting the player
            for m in meteor_array.sprites():
                if pygame.sprite.spritecollide(m, player_sprite, False, pygame.sprite.collide_mask):
                    if(player_sprite.sprite.hit()):
                        running = False
        else: 
            #otherwise see if invulnerability has worn off   
            player_sprite.sprite.check_invulnerable(dt)
            

                    
        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 30
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(30) / 1000
    return score_manager.current_score
    
    