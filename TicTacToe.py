import tkinter as tk
from tkinter import messagebox

def check_winner():
    # Check for winning combinations
    for combo in [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "":
            buttons[combo[0]].config(bg="green")
            buttons[combo[1]].config(bg="green")
            buttons[combo[2]].config(bg="green")
            messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[combo[0]]['text']} wins!")
            disable_all_buttons()
            return True
    
    # Check for draw - all buttons filled but no winner
    if all(button["text"] != "" for button in buttons):
        messagebox.showinfo("Tic-Tac-Toe", "It's a draw! All positions filled.")
        disable_all_buttons()
        return True
    
    return False

def button_click(index):
    global winner
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = current_player
        winner = check_winner()
        if not winner:
            toggle_player()

def toggle_player():
    global current_player
    current_player = "X" if current_player == "O" else "O"
    label.config(text=f"Player {current_player}'s turn")

def disable_all_buttons():
    for button in buttons:
        button.config(state="disabled")

def reset_game():
    global current_player, winner
    current_player = "X"
    winner = False
    for button in buttons:
        button.config(text="", bg="SystemButtonFace", state="normal")
    label.config(text=f"Player {current_player}'s turn")

root = tk.Tk()
root.title("Tic-Tac-Toe")

buttons = [tk.Button(root, text="", font=("normal", 25), width=6, height=2,
                     command=lambda i=i: button_click(i)) for i in range(9)]

for i, button in enumerate(buttons):
    button.grid(row=i//3, column=i%3)

current_player = "X"
winner = False
label = tk.Label(root, text=f"Player {current_player}'s turn", font=("normal", 16))
label.grid(row=3, column=0, columnspan=3)

# Add reset button
reset_button = tk.Button(root, text="Reset Game", font=("normal", 12), 
                        command=reset_game, bg="lightblue")
reset_button.grid(row=4, column=0, columnspan=3, pady=10)

root.mainloop()
