from code.Game import Game

try:
    import curses
except ImportError:
    import windows-curses as curses  # Fallback para Windows

game = Game()
game.run()
