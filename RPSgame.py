from random import seed
from random import randint
import os

# clear the console
def clear():
    os.system('clear')
    
# generate and display random choice for CPU
def choiceCPU():
    cI = randint(1,3)
    if (cI == 1):
        print('ROCK')
    elif (cI == 2):
        print('PAPER')
    else:
        print('SCISSORS')
    return cI

# prompt player for their choice
def choicePlayer():
    print('>> ', end="")
    pI = int(input())
    clear()
    if (pI == 1):
        print('^ROCK VS ', end="")
    elif (pI == 2):
        print('^PAPER VS ', end="")
    else:
        print('^SCISSORS VS ', end="")
    return pI

# determine winner of current round and update stats
def fight(pI, cI, stats):
    if (pI == cI):
        print('DRAW.')
        wOl = 'DRAW.'
        updateStats(stats, pI, cI, wOl)
    elif ((pI == 1 and cI == 3) or (pI == 2 and cI == 1) or (pI == 3 and cI == 2)):
        print('YOU WIN!')
        wOl = 'YOU WIN!'
        updateStats(stats, pI, cI, wOl)
    else:
        print('YOU LOSE')
        wOl = 'YOU LOSE'
        updateStats(stats, pI, cI, wOl)
        
# update statistics using choices and outcome of current round
def updateStats(stats, pI, cI, wOl):
    if (pI == 1):
        pI = 'ROCK'
    elif (pI == 2):
        pI = 'PAPER'
    else:
        pI = 'SCISSORS'
    
    if (cI == 1):
        cI = 'ROCK'
    elif (cI == 2):
        cI = 'PAPER'
    else:
        cI = 'SCISSORS'
    
    stats.append(pI + ' VS ' + cI + '  | ' + wOl + ' | ')
        
# main game loop
stats = []
cI = 1
while (cI == 1):    
    underline = '\033[4m'
    end = '\033[0m'
    clear()
    print(underline + '     CHOOSE YOUR FIGHTER!     ' + end + '\n|ROCK[1]|PAPER[2]|SCISSORS[3]|')
    pI = choicePlayer()
    cI = choiceCPU()
    fight(pI, cI, stats)
    print('Play Again? (yes[1] OR no[2])')
    print('>> ', end="")
    cI = int(input())

# display final game stats
clear()
print(underline + 'STATS' + end)
for x in stats:
    print('\n' + x)
print('\nBYE!')