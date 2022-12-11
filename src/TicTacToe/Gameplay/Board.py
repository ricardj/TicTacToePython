from ApplicationEngine.RenderManager import Renderable
from TicTacToe.Gameplay.Piece import Piece


class BoardCell(Renderable):
    piece_id: int = 0
    is_piece_filled: bool = False
    current_piece: Piece = None

    def __init__(self, piece_id):
        self.piece_id = piece_id

    def initialize(self):
        self.is_piece_filled = False
        self.current_piece = None

    def play_piece(self, piece):
        self.is_piece_filled = True
        self.current_piece = piece

    def render(self) -> str:
        return str(self.piece_id) if self.is_piece_filled else self.current_piece.skin()


class Board:
    board_cells = [BoardCell(x) for x in range(9)]

    def initialize(self):
        for cell in self.board_cells: cell.initialize()
        pass

    def render(self):
        result = ""
        for i, board_cell in enumerate(self.board_cells):
            render_value = str(
                board_cell.piece_id) if not board_cell.is_piece_filled else board_cell.current_piece.get_skin()
            result += "|" + render_value + "|"
            if (i + 1) % 3 == 0:
                result += "\n"

        return result

    def is_piece_empty(self, piece_id):
        return piece_id in self.get_empty_cell_ids()

    def play_piece(self, piece_id, piece):
        found_cell = next(cell for cell in self.board_cells if cell.piece_id == piece_id)
        found_cell.play_piece(piece)
        pass

    def get_empty_cell_ids(self):
        return [cell.piece_id for cell in self.board_cells if not cell.is_piece_filled]
        pass

    def get_winning_piece(self) -> Piece:
        # horizontal considerations
        groups_to_check = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6]
        ]
        for group in groups_to_check:
            group_pieces = [self.board_cells[i].current_piece for i in group]
            if group_pieces.count(group_pieces[0]) == len(group_pieces):
                return group_pieces[0]

        return None
