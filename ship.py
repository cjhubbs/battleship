class Ship():

    HORIZONTAL = 0;
    VERTICAL = 1;

    def __init__(self, size, name):
        self.size = size
        self.name = name
        self.locations = [[-1,-1] for i in range(size)]
        self.sunk = False
        self.position_assigned = False

    def overlap_exists(self,ships):
        #iterate over all ships
        for s in range(len(ships)):
            if ships[s] != self:
                #print("checking against " + repr(ships[s].name))
                #iterate over all positions in each ship
                for j in range(ships[s].size):
                    #iterate over all positions in self
                    for k in range(self.size):
                        if self.locations[k] == ships[s].locations[j]:
                            print("overlap at " + repr(self.locations[k]))
                            return True
        return False

    def set_position(self,x, y,orientation,ships):
        if x > 9 or y > 9:
            print("x pos out of bounds")
            return True
        if x < 0 or y < 0:
            print("y pos out of bounds")
            return True
        if orientation == self.HORIZONTAL and x + self.size > 9:
            print("x past edge of board")
            return True
        if orientation == self.VERTICAL and y + self.size > 9:
            print("y past edge of board")
            return True
        temp_x = x
        temp_y = y
        for i in range(self.size):
            self.locations[i] = [temp_x, temp_y]
            #print(repr(self.locations[i]))
            if orientation == self.HORIZONTAL:
                temp_x += 1
            else:
                temp_y += 1

        if self.overlap_exists(ships):
            print("overlap found!")
            for i in range(self.size):
                self.locations[i] = [-1,-1]
            return True
        else:
            #print("successfully positioned")
            self.position_assigned = True
            return False
