import os
clear = lambda: os.system('cls')
from cell import Cell
from ship import Ship

class Board:

    def __init__(self):
        self.board = [[Cell(i, j) for j in range(10)] for i in range(10)]
        self.hit_counter = 0
        self.needed_hits = 0

    def display(self):
        clear()
        for row in self.board:
            print(row[0].disp(), row[1].disp(), row[2].disp(), row[3].disp(), row[4].disp(), row[5].disp(), row[6].disp(), row[7].disp(), row[8].disp(), row[9].disp())

    def set_ships(self,ships):
        for s in range(len(ships)):
            for x,y in ships[s].locations:
                self.board[x][y].set_ship(True)
                self.needed_hits += 1

    def all_ships_sunk(self):
        if self.hit_counter == self.needed_hits:
            return True
        return False

    def shoot(self, shot_x, shot_y):
        if self.board[shot_x][shot_y].shoot():
            self.hit_counter += 1
            return True
        else:
            return False
