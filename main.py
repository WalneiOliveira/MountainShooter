import sys
import pygame
from code.Game import Game

try:
    import curses
except ImportError:
    try:
        import windows_curses as curses
    except ImportError:
        curses = None


def main():
    game = Game()
    game.run()

    # Garante que o pygame será encerrado corretamente
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()