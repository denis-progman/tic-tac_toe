from area import Area
from player import Player
from auto_player import AutoPlayer
from intelligent_auto_player import IntelligentAutoPlayer
from tictactoe import TicTacToe

class Launcher:
    DEFAULT_GAME_SIZE = 3

    def __init__(self):
        board_size = int(input('What board size do you want? ') or self.DEFAULT_GAME_SIZE)
        self.area = Area(board_size)
        self.players = [
            # Player("X", board_size),
            # Player("Y"), # We can have so many players that we want
            # AutoPlayer("#", board_size),
            AutoPlayer("$", board_size), # And auto players!
            AutoPlayer("@", board_size),
            # AutoPlayer("&"),
            IntelligentAutoPlayer("Q", board_size, 1)
            # Player("J"),
        ]

    def start(self):
        try: 
            game = TicTacToe(self.area, self.players)
            game.play()
        except Warning as warning:
            print(warning)
        # except BaseException as error:
        #     print(f'Ups! it\'s some unusual error. We are really sorry!\n\n{error}')
