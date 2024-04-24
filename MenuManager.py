from time import sleep
import pygame
import pygame_menu
from pygame_menu import themes
import pygame_menu.widgets
import pygame_menu.widgets.widget
import pygame_menu.widgets.widget.frame
import pygame_menu.widgets.widget.surface
import pygame_menu.widgets.widget.table
import pygame_menu.widgets.widget.textinput
import GameManager
import ScoreManager as sm


pygame.init()
surface = pygame.display.set_mode((1280, 720))
 
def start_the_game():
    mainmenu._open(GameManager.StartGame(game_over))
    test = initials_text.get_value()

    
def high_score_menu():
    mainmenu._open(high_scores)

mainmenu = pygame_menu.Menu('Welcome', 1280, 720, theme=themes.THEME_SOLARIZED)
initials_text = mainmenu.add.text_input('Please enter your initials:', default='AAA', maxchar=3)
mainmenu.add.button('Play', start_the_game)
mainmenu.add.button('High Scores', high_score_menu)
mainmenu.add.button('Quit', pygame_menu.events.EXIT)

high_scores = pygame_menu.Menu('High Scores', 1280, 720, theme=themes.THEME_GREEN)
scores = sm.ScoreManager(surface)
for score in scores.high_scores:
    score_line = high_scores.add.frame_h(800,50)
    initials = high_scores.add.label(score['initials'])
    val = high_scores.add.label(score['score'])
    score_line.relax(True)
    score_line.pack((initials,val), align=pygame_menu.locals.ALIGN_CENTER)

game_over = pygame_menu.Menu('Game Over', 1280,720, theme=themes.THEME_ORANGE)
go_score = game_over.add.frame_h(500,50)
game_over.add.label('Score')

arrow = pygame_menu.widgets.LeftArrowSelection(arrow_size = (10, 15))
 


while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()

    if mainmenu.is_enabled():
        mainmenu.update(events)
        mainmenu.draw(surface)
        if (mainmenu.get_current().get_selected_widget()):
            arrow.draw(surface, mainmenu.get_current().get_selected_widget())
 
    pygame.display.update()