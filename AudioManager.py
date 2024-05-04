import pygame

# initialize the mixer module
pygame.mixer.init()

# Load sounds for ship and meteor collision
ship_sound = pygame.mixer.Sound("ship.mp3")
collision = pygame.mixer.Sound("collision.ogg") #Todo Balance volume of crash and alarm sound effects in Audacity

def start_ship(ship_sound):
    ship_sound.play()
    return

def stop_ship(ship_sound):
    ship_sound.stop()
    return

def start_collision(collision):
    collision.play()
    return

def stop_collision(collision):
    collision.stop()
    return
