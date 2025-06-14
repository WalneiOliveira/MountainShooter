import sys
from datetime import datetime

import pygame
from pygame import Surface, Rect, KEYDOWN, K_RETURN, K_BACKSPACE, K_ESCAPE
from pygame.font import Font

from code.Const import C_YELLOW, SCORE_POS, MENU_OPTION, C_WHITE
from code.DBProxy import DBProxy


class Score:
    """Class to handle the score screen in the game."""

    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('./asset/ScoreBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)
        pass

    def save(self, game_mode: str, player_score: list[int]):
        """
        This method displays the score screen, prompts the player to enter their name.
        It saves the player's score to the database and allows them to view the top scores.

        params:
            game_mode (str): The game mode selected by the player.
            player_score (list[int]): The scores of the players or teams.
        """
        pygame.mixer_music.load('./asset/Score.mp3')
        pygame.mixer_music.play(-1)
        db_proxy = DBProxy('DBScore')
        name = ''
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.score_text(48, 'YOU WIN!!', C_YELLOW, SCORE_POS['Title'])
            text = 'Enter Player 1 name (4 characters):'
            score = player_score[0]
            if game_mode == MENU_OPTION[0]:
                score = player_score[0]
            if game_mode == MENU_OPTION[1]:
                score = (player_score[0] + player_score[1]) / 2
                text = 'Enter Team name (4 characters):'
            if game_mode == MENU_OPTION[2]:
                if player_score[0] >= player_score[1]:
                    score = player_score[0]
                else:
                    score = player_score[1]
                    text = 'Enter Player 2 name (4 characters):'
            self.score_text(20, text, C_WHITE, SCORE_POS['EnterName'])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_RETURN and len(name) == 4:
                        db_proxy.save({'name': name, 'score': score, 'date': get_formatted_date()})
                        self.show()
                        return
                    elif event.key == K_BACKSPACE:
                        name = name[:-1]
                    else:
                        if len(name) < 4:
                            name += event.unicode
            self.score_text(20, name, C_WHITE, SCORE_POS['Name'])
            pygame.display.flip()
            pass

    def show(self):
        """Display the top 10 scores from the database."""
        pygame.mixer_music.load('./asset/Score.mp3')
        pygame.mixer_music.play(-1)
        running = True
        while running:
            self.window.blit(source=self.surf, dest=self.rect)
            self.score_text(48, 'TOP 10 SCORE', C_YELLOW, SCORE_POS['Title'])
            self.score_text(20, 'NAME     SCORE           DATE', C_YELLOW, SCORE_POS['Label'])
            db_proxy = DBProxy('DBScore')
            list_score = db_proxy.retrieve_top10()
            db_proxy.close()
            for idx, player_score in enumerate(list_score):
                id_, name, score, date = player_score
                self.score_text(20, f'{name}     {score:05d}     {date}', C_YELLOW, SCORE_POS[idx])
            self.score_text(18, 'Pressione ESC para retornar | Pressione D para apagar todos os scores',
                            C_WHITE,
                            (self.window.get_width() // 2, self.window.get_height() - 30))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return
                    elif event.unicode.lower() == 'd':
                        db_proxy = DBProxy('DBScore')
                        db_proxy.clear_all()
                        db_proxy.close()
                        # Atualiza a tela após apagar
                        break

    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        """Render text on the score screen.

        params:
            text_size (int): The size of the text.
            text (str): The text to be displayed.
            text_color (tuple): The color of the text in RGB format.
            text_center_pos (tuple): The center position of the text on the screen.
        """
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)


def get_formatted_date():
    """Get the current date and time formatted as 'HH:MM - DD/MM/YY'."""
    current_datetime = datetime.now()
    current_time = current_datetime.strftime("%H:%M")
    current_date = current_datetime.strftime("%d/%m/%y")
    return f"{current_time} - {current_date}"
