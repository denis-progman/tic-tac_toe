from area import Area
from player import Player
from auto_player import AutoPlayer
from tictactoe import TicTacToe

class Launcher:
    DEFAULT_GAME_SIZE = 3

    def __init__(self):
        board_size = int(input('What board size do you want? ') or self.DEFAULT_GAME_SIZE)
        self.area = Area(board_size)
        self.players = [
            Player("X"),
            AutoPlayer("0"),
            # Player("Y"), # We can have so many players that we want
            AutoPlayer("$"), # And auto players!
            # Player("J"),
        ]

    def start(self):
        game = TicTacToe(self.area, self.players)
        game.play()
