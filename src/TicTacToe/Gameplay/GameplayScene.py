import random

from ApplicationEngine.SceneManager import Scene
from Observer.Observer import Event
from TicTacToe.Gameplay.Board import Board
from TicTacToe.Gameplay.Piece import Piece
from TicTacToe.Gameplay.Player import Player


class GameplayScene(Scene):
    # Game elements
    board = Board()
    player_user = Player("Player")
    player_enemy = Player("AI")

    # Game state
    current_player = None
    is_game_finished = False
    is_result_shown = False

    # Events
    on_change_scene: Event = Event()

    def __init__(self):
        pass

    def initialize(self):
        self.is_game_finished = False
        self.is_result_shown = False
        self.board.initialize()
        self.setup_player_pieces()
        self.current_player = self.choose_initial_player()

    def setup_player_pieces(self):
        piece_types = ["X", "O"]
        random.shuffle(piece_types)
        self.player_user.setup_piece(Piece(piece_types[0]))
        self.player_enemy.setup_piece(Piece(piece_types[1]))

    def choose_initial_player(self):
        return self.player_user if random.uniform(0, 1) > 0.5 else self.player_enemy

    def render(self) -> str:
        result = self.player_user.render() + "\n" + self.player_enemy.render() + "\n"
        result += self.board.render()
        if self.is_game_finished:
            winning_piece = self.board.get_winning_piece()
            if winning_piece is self.player_user.get_piece():
                result += "YOU WON!"
            elif winning_piece is self.player_enemy.get_piece():
                result += "You lost."
            else:
                result += "Is a draw"
        return result

    def update(self):
        if self.is_result_shown:
            input("Press enter to continue...")
            self.change_scene()

        if self.is_game_finished:
            self.is_result_shown = True

        if len(self.board.get_empty_cell_ids()) > 0 and self.board.get_winning_piece() is None:
            if self.current_player is self.player_user:
                piece_id = int(input("Select a cell to play piece: "))
                if self.board.is_piece_empty(piece_id):
                    self.board.play_piece(piece_id, self.current_player.get_piece())
                    self.current_player = self.player_enemy
            elif self.current_player is self.player_enemy:
                empty_cell_ids = self.board.get_empty_cell_ids()
                if len(empty_cell_ids) > 0:
                    piece_id = random.choice(empty_cell_ids)
                    self.board.play_piece(piece_id, self.current_player.get_piece())
                    self.current_player = self.player_user
        else:
            self.is_game_finished = True
