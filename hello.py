import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


playagain = True

while playagain:
    value = input('\nEnter a value:\n1.rock\n2.paper\n3.scissors\n')
    player = int(value)

    if player < 1 or player > 3:
        sys.exit("you must enter 1,2 or 3!")

    computer = random.randint(1, 3)

    print("You chose " + str(RPS(player)).replace('RPS.', '') + ".")
    print("CPU chose " + str(RPS(computer)).replace('RPS.', '') + ".")

    result = ''

    if player == 1:
        if computer == 1:
            result = 'Draw'
        elif computer == 2:
            result = 'Lose'
        else:
            result = 'Win'
    elif player == 2:
        if computer == 1:
            result = 'Win'
        elif computer == 2:
            result = 'Draw'
        else:
            result = 'Lose'
    else:
        if computer == 1:
            result = 'Lose'
        elif computer == 2:
            result = 'Win'
        else:
            result = 'Draw'

    print('The result is: ' + result + '.')
    print(RPS(2).value)

    playagain = input("\nPlay again?\nPress Y for 'Yes'.\nPress X for 'No'.\n")

    if playagain.lower() == 'y':
        continue
    else:
        playagain = False

sys.exit('Bye! \U0001F603')
