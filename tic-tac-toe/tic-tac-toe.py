import tkinter as tk
from tkinter import messagebox

# Game Logic Variables
# Tic Tac Toe generated by Gemini ai (not working correctly)




player1_name = "Player 1"
player2_name = "Player 2"
current_player = player1_name
board = [[" " for _ in range(3)] for _ in range(3)]
game_over = False

# GUI Functions
def check_winner():
    """Checks all winning combinations and declares a winner or tie."""
    global game_over, current_player
    # Check rows, columns, and diagonals
    for i in range(3):
        if (board[i][0] == board[i][1] == board[i][2] != " ") or \
           (board[0][i] == board[1][i] == board[2][i] != " "):
            messagebox.showinfo("Game Over", f"{current_player} wins!")
            game_over = True
            return

    # Check diagonals 
    if (board[0][0] == board[1][1] == board[2][2] != " ") or \
       (board[0][2] == board[1][1] == board[2][0] != " "):
        messagebox.showinfo("Game Over", f"{current_player} wins!")
        game_over = True
        return

    # Check for tie
    if all(cell != " " for row in board for cell in row):
        messagebox.showinfo("Game Over", "It's a tie!")
        game_over = True

def button_click(row, col):
    """Handles player input and updates the board."""
    global current_player, game_over
    if not game_over and board[row][col] == " ":
        buttons[row][col].config(text=current_player[0], state="disabled")  # Display player's initial
        board[row][col] = current_player[0]
        check_winner()

        if not game_over:  # Switch players
            current_player = player2_name if current_player == player1_name else player1_name
            turn_label.config(text=f"{current_player}'s Turn") 

def restart_game():
    """Resets the game board and state."""
    global current_player, board, game_over, player1_name, player2_name

    player1_name = name_entry1.get() or "Player 1"
    player2_name = name_entry2.get() or "Player 2"
    current_player = player1_name

    for row in range(3):
        for col in range(3):
            board[row][col] = " "
            buttons[row][col].config(text=" ", state="normal")
    game_over = False
    turn_label.config(text=f"{current_player}'s Turn") 

# GUI Setup
window = tk.Tk()
window.title("Tic-Tac-Toe")

# Name Entry
tk.Label(window, text="Player 1:").grid(row=0, column=0)
name_entry1 = tk.Entry(window)
name_entry1.grid(row=0, column=1)

tk.Label(window, text="Player 2:").grid(row=1, column=0)
name_entry2 = tk.Entry(window)
name_entry2.grid(row=1, column=1)

# Turn Display
turn_label = tk.Label(window, text=f"{current_player}'s Turn", font=('Arial', 12))
turn_label.grid(row=0, column=2, padx=10)

# Game Board Buttons
buttons = [[tk.Button(window, text=" ", font=('Arial', 20), width=3, height=1, 
                      command=lambda r=row, c=col: button_click(r, c))
            for col in range(3)] 
           for row in range(3)]

for row in range(3):
    for col in range(3):
        buttons[row][col].grid(row=row+2, column=col)

# Restart Button
restart_button = tk.Button(window, text="Restart", command=restart_game)
restart_button.grid(row=5, column=1, columnspan=2, sticky="WE")

window.columnconfigure(1, weight=1) 
window.mainloop()
