class Cell:

    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.has_ship = False
        self.hit = False
        self.miss = False
        self.row = -1
        self.col = "Z"

    def disp(self):
        if self.hit:
            return "X"
        if self.miss:
            return "0"
        if self.has_ship:
            return "1"
        return "-"

    def set_ship(self, state):
        self.has_ship = state

    def shoot(self):
        if self.has_ship:
            self.hit = True
        else:
            self.miss = True
        return self.hit
