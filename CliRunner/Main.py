import keyboard
import time
import os

was_pressed = False

# Function to execute when any key is pressed
def on_any_key_pressed(e):
    global was_pressed
    was_pressed = True

# Hook any key press event
keyboard.on_press(on_any_key_pressed)

class Player:

    def __init__(self):
        self.y_location = 8
        self.momentum = 0

    def getlocation(self):
        return self.y_location
    
    def getmomentum(self):
        return self.momentum

class Board:

    def __init__(self):
        self.board = [
            [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",],
            [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",],
            [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",],
            [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",],
            [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",],
            [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",],
            [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",],
            [" ", "8", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "8", " ", " ", " ",],
            [" ", "8", "8", " ", " ", " ", " ", " ", " ", " ", " ", " ", "8", " ", " ", " ",]
        ]

    def cycle_board(self):
        first_col = []

        for row in self.board:
            first_col.append(row[0])

        for row in self.board:
            for tile, _ in enumerate(row):
                try:
                    row[tile] = row[tile + 1]
                except IndexError:
                    break
        
        for row in self.board:
            row[-1] = first_col.pop(0)

    def printboard(self, player):
        player_y_location = player.getlocation()
        player_momentum = player.getmomentum()

        for rownum, row in enumerate(self.board):
            for colnum, _ in enumerate(row):
                if rownum == player_y_location and colnum == 6 - player_momentum:  # Adjust based on momentum
                    if self.board[rownum][6] != " ":
                        raise Exception("Game Over")
                    else:
                        print("O", end="")
                else:
                    print(self.board[rownum][colnum], end="")
            print()

try:

    score = 0

    player = Player()
    board = Board()

    while True:
        if was_pressed and player.getmomentum() == 0:
            player.momentum = 3
            was_pressed = False
        
        if player.getmomentum() > 0:
            player.momentum -= 1
            player.y_location -= 1
        else:
            if player.getlocation() != 8:
                player.y_location += 1

        board.cycle_board()
        board.printboard(player)

        if player.getlocation() == 8:
            score += 100
        
        print(f"Score: {score}")

        time.sleep(0.2)
        
        os.system('cls' if os.name == 'nt' else 'clear')

except KeyboardInterrupt:
    exit()
except Exception as e:
    print(e)
    exit()
finally:
    # Clean up and remove the hook when done
    keyboard.unhook_all()
