import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


playagain = True

dict = {
    '11': 'Draw',
    '12': 'Lose',
    '13': 'Win',
    '21': 'Win',
    '22': 'Draw',
    '23': 'Lose',
    '31': 'Lose',
    '32': 'Win',
    '33': 'Draw'
}

while playagain:
    value = input('\nEnter a value:\n1.rock\n2.paper\n3.scissors\n')
    player = int(value)

    if player < 1 or player > 3:
        sys.exit("you must enter 1,2 or 3!")

    computer = random.randint(1, 3)

    print("You chose " + str(RPS(player)).replace('RPS.', '') + ".")
    print("CPU chose " + str(RPS(computer)).replace('RPS.', '') + ".")

    result = dict[f'{player}{computer}']

    print('The result is: ' + result + '.')

    playagain = input("\nPlay again?\nPress Y for 'Yes'.\nPress X for 'No'.\n")

    if playagain.lower() == 'y':
        continue
    else:
        playagain = False

sys.exit('Bye! \U0001F603')
