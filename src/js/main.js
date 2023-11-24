let game_state = {
    board: [
        ["", "", ""],
        ["", "", ""],
        ["", "", ""],
    ],
    turn: "X",
    winner: null,
    message: "",
};

const form = document.getElementById("ticTacToeForm");
const messageElement = document.getElementById("message");

async function makeMove(row, col) {
    try {
        game_state.message = "";
        const response = await fetch("http://localhost:8000/api/makeMove", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ row, col, ...game_state }),
        });
        game_state = await response.json();
        updateBoard(game_state);
    } catch (error) {
        console.error("Error:", error);
    }
}

function resetGame() {
    game_state = {
        board: [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""],
        ],
        turn: "X",
        winner: null,
        message: "",
    };
    updateBoard(game_state);
}

function updateBoard(data) {
    if (!form) return;
    const buttons = form.getElementsByTagName("button");
    for (let i = 0; i < buttons.length; i++) {
        const [row, col] = buttons[i].id.split("").map(Number);
        buttons[i].textContent = data.board[row][col];
        if (data.winner) {
            buttons[i].disabled = true;
        } else {
            buttons[i].disabled = false;
        }
    }
    updateMessage(data);
}

function updateMessage(data) {
    if (!messageElement) return;
    if (data.winner) {
        messageElement.textContent =
            data.winner === "Tie" ? "It's a tie!" : `${data.winner} wins!`;
    } else if (data.message) {
        messageElement.textContent = `Your turn: ${data.turn} (Invalid move)`;
    } else {
        messageElement.textContent = `Your turn: ${data.turn}`;
    }
}
