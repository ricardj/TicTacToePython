from TicTacToe.Gameplay.Piece import Piece


class Player:
    piece: Piece = None
    player_name = "[NO NAME]"

    def __init__(self, player_name):
        self.player_name = player_name

    def setup_piece(self, piece):
        self.piece = piece
        pass

    def render(self):
        return self.player_name + ": " + self.piece.get_skin()
        pass

    def get_piece(self):
        return self.piece
        pass
