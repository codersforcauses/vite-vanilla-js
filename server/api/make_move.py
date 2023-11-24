from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class Input(BaseModel):
    row: int
    col: int
    board: list[list[str]]
    turn: str
    winner: str | None
    message: str


class Result(BaseModel):
    board: list[list[str]]
    turn: str
    winner: str | None
    message: str


def check_winner(board):
    # Check rows, columns, and diagonals for a winner
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            return board[i][0]  # Row
        if board[0][i] == board[1][i] == board[2][i] != "":
            return board[0][i]  # Column
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]  # Diagonal
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]  # Diagonal
    return None


def is_board_full(board):
    # Check if the board is full
    for row in board:
        if "" in row:
            return False
    return True


@router.post("/api/makeMove", response_model=Result)
def make_move(state: Input):
    row = state.row
    col = state.col
    game_state = {
        "board": state.board,
        "turn": state.turn,
        "winner": state.winner,
        "message": state.message,
    }
    if game_state["board"][row][col] == "" and game_state["winner"] is None:
        game_state["board"][row][col] = game_state["turn"]
        winner = check_winner(game_state["board"])
        if winner:
            game_state["winner"] = winner
        elif is_board_full(game_state["board"]):
            game_state["winner"] = "Tie"
        else:
            game_state["turn"] = "O" if game_state["turn"] == "X" else "X"
    else:
        game_state["message"] = "Invalid move"
    return game_state
