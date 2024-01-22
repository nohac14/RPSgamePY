from random import seed
from random import randint
import os

def clear():
    os.system('clear')
    
def choiceCPU():
    cI = randint(1,3)
    if (cI == 1):
        print('ROCK')
    elif (cI == 2):
        print('PAPER')
    else:
        print('SCISSORS')
    return cI

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
        
# main
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
clear()
print(underline + 'STATS' + end)
for x in stats:
    print('\n' + x)
print('\nBYE!')