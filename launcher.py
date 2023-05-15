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
            # Player("Y", board_size), # We can have so many players that we want
            IntelligentAutoPlayer("Q", board_size, 5),
            AutoPlayer("#", board_size),
            AutoPlayer("$", board_size), # And auto players!
            # AutoPlayer("@", board_size),
            # AutoPlayer("&", board_size),
            # Player("J", board_size),
        ]

    def start(self):
        try: 
            game = TicTacToe(self.area, self.players)
            game.play()
        except Warning as warning:
            print(warning)
        # except BaseException as error:
        #     print(f'Ups! it\'s some unusual error. We are really sorry!\n\n{error}')
