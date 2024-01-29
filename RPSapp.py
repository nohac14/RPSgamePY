from tkinter import *
# from tkinter.ttk import *
import RPSgame

root = Tk()

def rock():
    cI = RPSgame.choiceCPUapp()
    result = RPSgame.fightApp(1, cI, stats)
    resultL = Label(root, text=result)

def paper():
    cI = RPSgame.choiceCPUapp()
    result = RPSgame.fightApp(2, cI, stats)
    resultL = Label(root, text=result)
    
def scissors():
    cI = RPSgame.choiceCPUapp()
    result = RPSgame.fightApp(3, cI, stats)
    resultL = Label(root, text=result)

stats = []
prompt = Label(root, text="CHOOSE YOUR FIGHTER!")
prompt.pack()
# photoR = PhotoImage(file = r"The_rock.png")
# rockB = Button(root, image=photoR, padx=50, pady=50)
rockB = Button(root, text="ROCK", command=rock)
paperB = Button(root, text="PAPER", command=paper)
scissorsB = Button(root, text="SCISSORS", command=scissors)
rockB.pack(side=LEFT)
paperB.pack(side=LEFT)
scissorsB.pack(side=LEFT)

root.mainloop()