import os
import sys

import pygame

from code.Game import Game

# Configuração especial para o PyInstaller
if getattr(sys, 'frozen', False):
    os.chdir(sys._MEIPASS)

try:
    import curses
except ImportError:
    try:
        import windows_curses as curses

        print("Using windows-curses fallback")
    except ImportError:
        print("Warning: curses not available - some features might not work")
        curses = None


def main():
    game = Game()
    game.run()


if __name__ == "__main__":
    main()
