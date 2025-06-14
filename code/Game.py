#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION, SCORE_POS
from code.Level import Level
from code.Menu import Menu
from code.Score import Score


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self) -> None:
        """ Run the game loop
        :param self: Instance of the Game class
        :return: None"""
        pygame.display.set_caption('Wellcome to our Game!!')
        self.window.fill((0, 0, 0))
        while True:
            score = Score(self.window)
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                player_score = [0, 0]  # Player scores for multiplayer

                level = Level(self.window, 'Level1', menu_return, player_score)
                level_return = level.run(player_score)

                if level_return:
                    level = Level(self.window, 'Level2', menu_return, player_score)
                    level_return = level.run(player_score)
                    if level_return:
                        level = Level(self.window, 'Level3', menu_return, player_score)
                        level_return = level.run(player_score)
                        if level_return:
                            score.save(menu_return, player_score)
            elif menu_return == MENU_OPTION[3]:
                score.show()
            elif menu_return == MENU_OPTION[4]:
                pygame.quit()  # Close Window
                sys.exit()  # end pygame
            else:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            pygame.quit()
                            sys.exit()
