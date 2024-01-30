import tkinter as tk
from tkinter import messagebox
import random
    
def createButton(root, text, command):
    return tk.Button(root, text=text, width=10, height=2, command=command)

def choiceCPU():
    return random.choice(["Rock", "Paper", "Scissors"])

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

def play(playerC):
    cpuC = choiceCPU()
    result = fight(playerC, cpuC)
    stats.append(playerC + " VS " + cpuC + "\n" + result + "\n")
    resultL["text"] = f"Player: {playerC}\nCPU: {cpuC}\n{result}"
    
def on_closing():
    result = messagebox.askquestion("Exit", "Do you want to exit and view stats?")
    if result == "yes":
        messagebox.showinfo("Stats", "\n".join(stats))
        root.destroy()

root = tk.Tk()

stats = []

root.iconbitmap("RPS.ico")
root.title("CHOOSE YOUR FIGHTER!")

resultL = tk.Label(root, text="")

rockB = createButton(root, text="ROCK", command=lambda: play("Rock"))
paperB = createButton(root, text="PAPER", command=lambda: play("Paper"))
scissorsB = createButton(root, text="SCISSORS", command=lambda: play("Scissors"))

resultL.grid(row=1, column=0, columnspan=3, pady=10)

rockB.grid(row=0, column=0, padx=10, pady=10)
paperB.grid(row=0, column=1, padx=10, pady=10)
scissorsB.grid(row=0, column=2, padx=10, pady=10)

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()

underline = '\033[4m'
end = '\033[0m'
print(underline + 'STATS' + end)
for x in stats:
    print('\n' + x)
print('\nBYE!')