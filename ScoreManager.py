import pygame
import json

class ScoreManager():

    #json_format
    #{
    #   "highscores"[
    #       {"initials": "score"},
    #       {"initials": "score"}
    #   ]
    #}
    
    high_scores: list   
    current_score: int
    screen: pygame.surface
    score_font: pygame.font
    score_text: pygame.surface
    score_pos: pygame.rect

    def __init__(self, screen: pygame.surface):
        self.score_font = pygame.font.Font(size= 30)
        self.screen = screen
        self.current_score = 0
        self.high_scores = list()
        self.score_text = self.score_font.render( f"Score: {self.current_score}",False, (255,255,255))
        self.score_pos = (self.screen.get_bounding_rect().right - self.score_text.get_width() - 20, 20)

    def load_scores(self):
        """
        Loads the high scores from the high_scores.json file
        Sorts based on the score in reverse order, so the highest is first.
        """
        with open("high_scores.json") as hs:
            scores = json.load(hs)
            self.high_scores = sorted(scores["highscores"], key=lambda d: d["score"], reverse=True)
            

    def draw(self):
        """
        Draws the score in the top right of the screen.
        """
        self.score_text = self.score_font.render( f"Score: {self.current_score}",False, (255,255,255))
        self.score_pos = (self.screen.get_bounding_rect().right - self.score_text.get_width() - 20, 20)
        return self.score_text, self.score_pos

    def save_scores(self):
        """
        Creates a list of dictionary items based on the high scores
            and saves them to high_scores.json
        """
        highscores = {}
        highscores["highscores"]= self.high_scores
        with open("high_scores.json", "w") as hs:
            json.dump(highscores, hs)