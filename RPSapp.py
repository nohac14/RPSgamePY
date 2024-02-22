import tkinter as tk
from tkinter import messagebox
import random
    
# create button with specified text and command
def createButton(root, text, command):
    return tk.Button(root, text=text, width=10, height=2, command=command)

# generate random choice for CPU
def choiceCPU():
    return random.choice(["Rock", "Paper", "Scissors"])

# determine winner of current round
def fight(playerC, cpuC):
    if playerC == cpuC:
        return "It's a tie!"
    elif (
        (playerC == "Rock" and cpuC == "Scissors") or
        (playerC == "Paper" and cpuC == "Rock") or
        (playerC == "Scissors" and cpuC == "Paper")
    ):
        return "You win!"
    else:
        return "CPU wins!"

# handle player choice and update game stats
def play(playerC):
    cpuC = choiceCPU()
    result = fight(playerC, cpuC)
    stats.append(playerC + " VS " + cpuC + "\n" + result + "\n")
    resultL["text"] = f"Player: {playerC}\nCPU: {cpuC}\n{result}"
    update_stats_text()

# updae game stats displayed in the window
def update_stats_text():
    stats_text.config(state=tk.NORMAL)
    stats_text.delete(1.0, tk.END)
    stats_text.insert(tk.END, "\n".join(stats))
    stats_text.config(state=tk.DISABLED)

# handle window closing
def on_closing():
    root.destroy()

stats = []

# main window
root = tk.Tk()

# window settings
root.iconbitmap("RPS.ico")
root.title("Rock, Paper, Scissors, SHOOT!")

# label to display current round result
resultL = tk.Label(root, text="")

# buttons
rockB = createButton(root, text="ROCK", command=lambda: play("Rock"))
paperB = createButton(root, text="PAPER", command=lambda: play("Paper"))
scissorsB = createButton(root, text="SCISSORS", command=lambda: play("Scissors"))

# grid layout for widgets
resultL.grid(row=1, column=0, columnspan=3, pady=10)
rockB.grid(row=0, column=0, padx=10, pady=10)
paperB.grid(row=0, column=1, padx=10, pady=10)
scissorsB.grid(row=0, column=2, padx=10, pady=10)

# scrollbar and text widgets to display stats
scrollbar = tk.Scrollbar(root)
scrollbar.grid(row=2, column=3, sticky=tk.NS)

stats_text = tk.Text(root, wrap=tk.WORD, yscrollcommand=scrollbar.set, state=tk.DISABLED)
stats_text.grid(row=2, column=0, columnspan=3, pady=10)

scrollbar.config(command=stats_text.yview)

# set window closing event handler
root.protocol("WM_DELETE_WINDOW", on_closing)

# start loop for Tkinter window
root.mainloop()

# display final game stats in console
underline = '\033[4m'
end = '\033[0m'
print(underline + 'STATS' + end)
for x in stats:
    print('\n' + x)
print('\nBYE!')