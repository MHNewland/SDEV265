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
current_score = 0
scores = sm.ScoreManager(surface)
 
def start_the_game():
    global current_score
    current_score = GameManager.StartGame()
    game_over.get_widget("score_val",True).set_title(current_score)
    mainmenu._open(game_over)

def high_score_menu():
    if(mainmenu.get_current().get_title() == "Game Over"):
        save_score()

    score_frame = high_scores.get_widget("score_frame")
    for widget in score_frame.get_widgets():
        high_scores.remove_widget(widget)

    score_frame.clear()
    scores.load_scores()
    for score in scores.high_scores:
        score_line = high_scores.add.frame_h(800,50)
        initials = high_scores.add.label(score['initials'])
        val = high_scores.add.label(score['score'])
        score_line.relax(True)
        score_line.pack((initials,val), align=pygame_menu.locals.ALIGN_CENTER)
        score_frame.pack(score_line)
    
    mainmenu._open(high_scores)

def play_again():
    save_score()
    start_the_game()

def save_score():
    scores.high_scores.append({"initials": initials_text.get_value(), "score":current_score})
    scores.high_scores.sort(key=lambda d: d["score"], reverse=True)
    scores.high_scores=scores.high_scores[:10]
    scores.save_scores()

def main_menu():
    if(mainmenu.get_current().get_title() == "Game Over"):
        save_score()
    mainmenu._back()

mainmenu = pygame_menu.Menu('Welcome', 1280, 720, theme=themes.THEME_SOLARIZED)
mainmenu.add.button('Play', start_the_game)
mainmenu.add.button('High Scores', high_score_menu)
mainmenu.add.button('Quit', pygame_menu.events.EXIT)



game_over = pygame_menu.Menu('Game Over', 1280,720, theme=themes.THEME_ORANGE)
initials_text = game_over.add.text_input('Please enter your initials:', default='AAA', maxchar=3)
go_score = game_over.add.frame_h(500,50)
score_lbl = game_over.add.label('Score: ')
score_val = game_over.add.label(current_score, "score_val")
go_score.relax(True)
go_score.pack((score_lbl, score_val), align=pygame_menu.locals.ALIGN_CENTER)
game_over.add.button("Play Again", play_again)
game_over.add.button("High Scores", high_score_menu)
game_over.add.button("Main Menu", main_menu)

high_scores = pygame_menu.Menu('High Scores', 1280, 720, theme=themes.THEME_GREEN)
score_frame = high_scores.add.frame_v(850,550,frame_id="score_frame")
high_scores.add.button("Main Menu", main_menu)

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