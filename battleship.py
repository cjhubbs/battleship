
import random
from time import sleep
from board import Board
from ship import Ship

#######################################################
def play_game():

    #initialize 10x10 matrix to 0
    shots = [[0 for j in range(10)] for i in range(10)]

    b = Board()

    #ships = []
    cruiser = Ship(2,"Cruiser")
    destroyer = Ship(3,"Destroyer")
    submarine = Ship(3,"Submarine")
    battleship = Ship(4,"Battleship")
    carrier = Ship(5,"Carrier")
    ships = [cruiser, destroyer, submarine, battleship, carrier]

    if cruiser.set_position(0,0,Ship.HORIZONTAL,ships):
        print("Error in setting position of cruiser")
    if destroyer.set_position(0,1,Ship.VERTICAL,ships):
        print("Error in setting position of destroyer")
    if submarine.set_position(3,3,Ship.HORIZONTAL,ships):
        print("Error setting position of submarine")
    if battleship.set_position(9,0,Ship.VERTICAL,ships):
        print("Error setting position of battleship")
    if carrier.set_position(4,8,Ship.HORIZONTAL,ships):
        print("Error setting position of carrier")

    b.set_ships(ships)

    #b.display()
    shot_counter = 0

    while not b.all_ships_sunk():
        shot_x = random.randint(0,9)
        shot_y = random.randint(0,9)

        while shots[shot_x][shot_y]:
            shot_x = random.randint(0,9)
            shot_y = random.randint(0,9)

        shots[shot_x][shot_y] = 1
        shot_counter += 1
        is_hit = b.shoot(shot_x,shot_y)
        #b.display()
        #sleep(0.3)

    return shot_counter

number_of_games = 100
total_shots = 0
counts = []
for i in range(number_of_games):
    counts.append(play_game())
    #print(repr(counts))
    print("Game " + repr(i) + " took " + repr(counts[i]) + " shots")
    total_shots += counts[i]

avg_shots = total_shots / number_of_games
print("Average shots required = " + repr(avg_shots))
