# Imports
import random
import os


# Draw grid
# Pick random location for player
# Pick random location for monster
# Draw player in grid
# Take input for movement
# Move player, unless invalid move (past edges of grid)
# Check for win/loss
# Clear screen and redraw grid

# Define grid
CELLS = [
    (0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
    (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
    (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
    (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),
    (0, 4), (1, 4), (2, 4), (3, 4), (4, 4),
]

# Functions
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_locations():
    return random.sample(CELLS, 3)


def move_player(player, move):
    # Get the player's location
    x, y = player

    # Left, x-1
    if move == 'LEFT':
        x -= 1

    # Right, x+1
    if move == 'RIGHT':
        x += 1

    # Up, y+1
    if move == 'UP':
        y -= 1

    # Down, y-1
    if move == 'DOWN':
        y += 1

    return x, y


def get_moves(player):
    moves = ["LEFT", "RIGHT", "UP", "DOWN"]

    # Unpack player tuple:
    x, y = player

    # Player's y==0, can't move up
    if y == 0:
        moves.remove("UP")

    # Player's y==4, can't move down
    if y == 4:
        moves.remove("DOWN")

    # Player's x==0, can't move left
    if x == 0:
        moves.remove("LEFT")

    # Player's x==4, can't move right
    if x == 4:
        moves.remove("RIGHT")

    return moves


def draw_map(player):
    print(" _" * 5)
    tile = "|{}"

    for cell in CELLS:
        x, y = cell
        if x < 4:
            line_end = ""
            if cell == player:
                output = tile.format("X")
            else:
                output = tile.format("_")
        else:
            line_end = "\n"
            if cell == player:
                output = tile.format("X|")
            else:
                output = tile.format("_|")
        print(output, end=line_end)


def game_loop():
    monster, door, player = get_locations()
    playing = True

    while playing:
        clear_screen()
        draw_map(player)
        valid_moves = get_moves(player)

        print("You're currently in room {}.".format(player))    # Fill with player position
        print("You can move {}".format(", ".join(valid_moves))) # Fill with available moves
        print("Enter QUIT to quit.")

        move = input(">  ").upper()

        if move == 'QUIT':
            print("\n**  See you next time!  **\n")
            break

        # Good move?  Change the player position.
        if move in valid_moves:
            player = move_player(player, move)

            # On the monster?  They lose.
            if player == monster:
                print("\n**  Oh no!  The monster got you!  Better luck next time!  **\n")
                # break
                playing = False

            # On the door?  They win.
            if player == door:
                print("\n**  You escaped!  Congratulations!  **\n")
                # break
                playing = False

            # Otherwise, loop back around.

        # Bad move?  Don't change anything.
        else:
            input("\n**  Walls are hard!  Don't run into them!  **\n")

    else:
        if input("Play again (Y/N)?  ").lower() != 'n':
            game_loop()

# BEGIN GAME
clear_screen()

print("Welcome to the dungeon!")
input("Press Enter to start.")

clear_screen()
game_loop()

