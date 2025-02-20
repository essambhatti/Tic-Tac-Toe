
import tkinter as tk
from tkinter import messagebox

dictionary = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9"}

# Function to update the board
def pattern():
    board_text.set(f"""
      {dictionary[1]} | {dictionary[2]} | {dictionary[3]}
     -----------
      {dictionary[4]} | {dictionary[5]} | {dictionary[6]}
     -----------
      {dictionary[7]} | {dictionary[8]} | {dictionary[9]}
    """)

def winner():
    if (dictionary[1] == "X" and dictionary[2] == "X" and dictionary[3] == "X") or \
       (dictionary[4] == "X" and dictionary[5] == "X" and dictionary[6] == "X") or \
       (dictionary[7] == "X" and dictionary[8] == "X" and dictionary[9] == "X") or \
       (dictionary[1] == "X" and dictionary[4] == "X" and dictionary[7] == "X") or \
       (dictionary[2] == "X" and dictionary[5] == "X" and dictionary[8] == "X") or \
       (dictionary[3] == "X" and dictionary[6] == "X" and dictionary[9] == "X") or \
       (dictionary[1] == "X" and dictionary[5] == "X" and dictionary[9] == "X") or \
       (dictionary[3] == "X" and dictionary[5] == "X" and dictionary[7] == "X"):
        return "1"
    elif (dictionary[1] == "O" and dictionary[2] == "O" and dictionary[3] == "O") or \
         (dictionary[4] == "O" and dictionary[5] == "O" and dictionary[6] == "O") or \
         (dictionary[7] == "O" and dictionary[8] == "O" and dictionary[9] == "O") or \
         (dictionary[1] == "O" and dictionary[4] == "O" and dictionary[7] == "O") or \
         (dictionary[2] == "O" and dictionary[5] == "O" and dictionary[8] == "O") or \
         (dictionary[3] == "O" and dictionary[6] == "O" and dictionary[9] == "O") or \
         (dictionary[1] == "O" and dictionary[5] == "O" and dictionary[9] == "O") or \
         (dictionary[3] == "O" and dictionary[5] == "O" and dictionary[7] == "O"):
        return "2"
    elif all(dictionary[i] in ["X", "O"] for i in range(1, 10)):
        return "3"

def click(position, player):
    if dictionary[position] not in ["X", "O"]:
        dictionary[position] = player
        buttons[position - 1].config(text=player, state=tk.DISABLED)
        result = winner()
        if result == "1":
            messagebox.showinfo("Game Over", "X is the winner!")
            reset_game()
        elif result == "2":
            messagebox.showinfo("Game Over", "O is the winner!")
            reset_game()
        elif result == "3":
            messagebox.showinfo("Game Over", "Game is a draw!")
            reset_game()
        return True
    else:
        messagebox.showerror("Invalid Move", "This spot is already taken!")
        return False

def player_turn(position):
    global current_player
    if click(position, current_player):
        current_player = "O" if current_player == "X" else "X"

def reset_game():
    global dictionary, current_player
    dictionary = {i: str(i) for i in range(1, 10)}
    for button in buttons:
        button.config(text="", state=tk.NORMAL)
    current_player = "X"
    pattern()

# Tkinter GUI Setup
root = tk.Tk()
root.title("Tic-Tac-Toe")
root.geometry("300x350")

display_frame = tk.Frame(root)
display_frame.pack()

board_text = tk.StringVar()
pattern()

title_label = tk.Label(display_frame, text="Tic-Tac-Toe", font=("Arial", 16, "bold"))
title_label.pack()

buttons = []

game_frame = tk.Frame(root)
game_frame.pack()

current_player = "X"

for i in range(3):
    for j in range(3):
        pos = i * 3 + j + 1
        btn = tk.Button(game_frame, text="", font=("Arial", 16), height=2, width=5,
                         command=lambda p=pos: player_turn(p))
        btn.grid(row=i, column=j)
        buttons.append(btn)

reset_button = tk.Button(root, text="Reset Game", font=("Arial", 12), command=reset_game)
reset_button.pack()

root.mainloop()
