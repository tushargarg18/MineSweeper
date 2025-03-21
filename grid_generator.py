import random
import json

class GridGenerator:
    def __init__(self, size=4, num_mines = 5):
        if (size > num_mines + (size//2)):
            self.size = size
            self.num_mines = num_mines
            self.grid = [[0 for _ in range(size)] for _ in range(size)]
            self._place_mines()
            self._calculate_adjacent_mines()
            print(self.grid)
        else:
            print("The size and mine number is not valid")

    def _place_mines(self):
        mine_pos = set()
        while len(mine_pos) < self.num_mines:
            x, y = random.randint(0,self.size-1), random.randint(0,self.size-1)
            if (x,y) not in mine_pos:
                mine_pos.add((x,y))
                self.grid[x][y] = 'x'
    
    def _calculate_adjacent_mines(self):
        directions = ((-1,-1), (-1,0), (-1,1), (0,1), (0,-1), (1, -1), (1,0), (1,1))
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j] == 'x':
                    continue
                else:
                    count = 0
                    for x,y in directions:
                        if (i-x < self.size and j-y < self.size) and (i-x >= 0 and j-y >= 0):
                            if self.grid[i-x][j-y] == 'x':
                                count += 1
                    self.grid[i][j] = count
    
    def save_grid(self, filename="grid.json"):
        with open(filename, "w") as f:
            json.dump({"size": self.size, "grid": self.grid}, f)
    
    def display(self):
        for row in self.grid:
            print(" ".join(str(cell) for cell in row))



if __name__ == "__main__":
    obj = GridGenerator(size=2, num_mines=5)
    obj.display()
    obj.save_grid()
