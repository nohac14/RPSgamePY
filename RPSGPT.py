import tkinter as tk
from tkinter import messagebox
import random

def choice_cpu():
    return random.choice(["Rock", "Paper", "Scissors"])

def determine_winner(player_choice, cpu_choice):
    if player_choice == cpu_choice:
        return "It's a tie!"
    elif (
        (player_choice == "Rock" and cpu_choice == "Scissors") or
        (player_choice == "Paper" and cpu_choice == "Rock") or
        (player_choice == "Scissors" and cpu_choice == "Paper")
    ):
        return "You win!"
    else:
        return "CPU wins!"

def play_game(player_choice):
    cpu_choice = choice_cpu()
    result = determine_winner(player_choice, cpu_choice)
    messagebox.showinfo("Result", f"Player: {player_choice}\nCPU: {cpu_choice}\n{result}")

def create_button(root, text, command):
    return tk.Button(root, text=text, width=10, height=2, command=command)

root = tk.Tk()
root.title("Rock, Paper, Scissors")

rock_button = create_button(root, "Rock", lambda: play_game("Rock"))
paper_button = create_button(root, "Paper", lambda: play_game("Paper"))
scissors_button = create_button(root, "Scissors", lambda: play_game("Scissors"))

rock_button.grid(row=0, column=0, padx=10, pady=10)
paper_button.grid(row=0, column=1, padx=10, pady=10)
scissors_button.grid(row=0, column=2, padx=10, pady=10)

root.mainloop()
