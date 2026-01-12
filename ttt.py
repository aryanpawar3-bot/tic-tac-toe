import tkinter as tk
from tkinter import messagebox

board = [""] * 9
current_player = "X"

def check_winner(player):
    wins = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    for a,b,c in wins:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

def is_draw():
    return "" not in board

def click(index):
    global current_player
    if board[index] == "":
        board[index] = current_player
        buttons[index]["text"] = current_player

        if check_winner(current_player):
            messagebox.showinfo("Game Over", f"Player {current_player} wins!")
            reset()
        elif is_draw():
            messagebox.showinfo("Game Over", "It's a Draw!")
            reset()
        else:
            current_player = "O" if current_player == "X" else "X"

def reset():
    global board, current_player
    board = [""] * 9
    current_player = "X"
    for btn in buttons:
        btn.config(text="")

root = tk.Tk()
root.title("Tic Tac Toe App")

buttons = []
for i in range(9):
    b = tk.Button(root, text="", font=("Arial", 24),
                  width=5, height=2,
                  command=lambda i=i: click(i))
    b.grid(row=i//3, column=i%3)
    buttons.append(b)

root.mainloop()
