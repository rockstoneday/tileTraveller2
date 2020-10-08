import random
# https://github.com/rockstoneday/tileTraveller2.git
# Constants
NORTH = 'n'
EAST = 'e'
SOUTH = 's'
WEST = 'w'

def move(direction, col, row):
    ''' Returns updated col, row given the direction '''
    if direction == NORTH:
        row += 1
    elif direction == SOUTH:
        row -= 1
    elif direction == EAST:
        col += 1
    elif direction == WEST:
        col -= 1
    return(col, row)    

def is_victory(col, row):
    ''' Return true if player is in the victory cell '''
    return col == 3 and row == 1 # (3,1)

def print_directions(directions_str):
    print("You can travel: ", end='')
    first = True
    for ch in directions_str:
        if not first:
            print(" or ", end='')
        if ch == NORTH:
            print("(N)orth", end='')
        elif ch == EAST:
            print("(E)ast", end='')
        elif ch == SOUTH:
            print("(S)outh", end='')
        elif ch == WEST:
            print("(W)est", end='')
        first = False
    print(".")

def coincount(col, row):
    if (col, row) in [(1,2), (2,2), (2,3), (3,2)]:
        print("Pull a lever (y/n): ")
        inn = random.choice(['y', 'n'])
        if inn == 'y' or inn == 'Y':
            total = 1
            return total
        else:
            return 0
    else:
        return 0

        
def find_directions(col, row):
    ''' Returns valid directions as a string given the supplied location '''
    if col == 1 and row == 1:   # (1,1)
        valid_directions = NORTH
    elif col == 1 and row == 2: # (1,2)
        valid_directions = NORTH+EAST+SOUTH
    elif col == 1 and row == 3: # (1,3)
        valid_directions = EAST+SOUTH
    elif col == 2 and row == 1: # (2,1)
        valid_directions = NORTH
    elif col == 2 and row == 2: # (2,2)
        valid_directions = SOUTH+WEST
    elif col == 2 and row == 3: # (2,3)
        valid_directions = EAST+WEST
    elif col == 3 and row == 2: # (3,2)
        valid_directions = NORTH+SOUTH
    elif col == 3 and row == 3: # (3,3)
        valid_directions = SOUTH+WEST
    return valid_directions

def play_one_move(col, row, valid_directions, coins):
    ''' Plays one move of the game
        Return if victory has been obtained and updated col,row '''
    victory = False
    print("Direction: ")
    direction = random.choice(['n', 'e', 's', 'w'])
    direction = direction.lower()
    
    if not direction in valid_directions:
        print("Not a valid direction!")
    else:
        col, row = move(direction, col, row)
        victory = is_victory(col, row)
        coins += coincount(col,row)
    return victory, col, row, coins


def play():
    victory = False
    row = 1
    col = 1
    coins = 0
    total = 1
    moves = 0
    seed = input("Input seed: ")

    while not victory:
        valid_directions = find_directions(col, row)
        print_directions(valid_directions)
        victory, col, row, coins = play_one_move(col, row, valid_directions, coins)
        if coins == total:
            print(f"You received 1 coin, your total is now {coins}.")
            total += 1
        moves += 1
    print(f"Victory! Total coins {coins}. Moves {moves}")
    replay = input("Play again (y/n): ")
    if replay == 'y' or replay == 'Y':
        play()
# The main program starts here
play()