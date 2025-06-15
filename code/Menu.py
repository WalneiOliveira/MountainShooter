#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, C_ORANGE, MENU_OPTION, C_WHITE, C_YELLOW, SCORE_POS, C_BLACK, C_ALPHA, PADDING


class Menu:
    """Class to handle the main menu of the game."""

    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        """
        Displays the main menu and allows navigation via keyboard or mouse.
        Returns the selected menu option.
        If the user selects an option, it returns the corresponding string.
        If the user quits, it exits the game.
        Returns: str: The selected menu option.
        """
        menu_option = 0
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.set_volume(0.1)
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Mountain Shooter", C_YELLOW, ((WIN_WIDTH / 2), 70))

            mouse_pos = pygame.mouse.get_pos()

            option_rects = []
            for i in range(len(MENU_OPTION)):
                rect = pygame.Rect(0, 0, 200, 30)  # Adjust width/height as needed
                rect.center = (int(WIN_WIDTH / 2), 200 + 25 * i)
                option_rects.append(rect)
                if rect.collidepoint(mouse_pos):
                    menu_option = i

            for i in range(len(MENU_OPTION)):
                color = C_YELLOW if i == menu_option else C_WHITE
                self.menu_text(20, MENU_OPTION[i], color, (int(WIN_WIDTH / 2), 200 + 25 * i))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.mixer.music.stop()
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        menu_option = (menu_option + 1) % len(MENU_OPTION)
                    elif event.key == pygame.K_UP:
                        menu_option = (menu_option - 1) % len(MENU_OPTION)
                    elif event.key == pygame.K_RETURN:
                        pygame.mixer.music.stop()
                        return MENU_OPTION[menu_option]
                    elif event.key == pygame.K_ESCAPE:
                        pygame.mixer.music.stop()
                        pygame.quit()
                        sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    for i, rect in enumerate(option_rects):
                        if rect.collidepoint(event.pos):
                            pygame.mixer.music.stop()
                            return MENU_OPTION[i]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        """Render text on the menu."""
        padding = PADDING
        frame_color = C_BLACK
        frame_alpha = C_ALPHA
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        frame_surf = pygame.Surface((text_rect.width + 2 * padding, text_rect.height + 2 * padding), pygame.SRCALPHA)
        frame_surf.fill((*frame_color, frame_alpha))
        self.window.blit(frame_surf, (text_rect.x - padding, text_rect.y - padding))
        self.window.blit(text_surf, text_rect)
