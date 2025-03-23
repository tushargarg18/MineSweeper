import json
import random
from grid_generator import GridGenerator

class Game_Logic:
    def __init__(self, filename="grid.json"):
        with open(filename, "r") as f:
            data = json.load(f)
        self.size = data["size"]
        self.grid = data["grid"]
        self.revealed = [[False for _ in range(self.size)] for _ in range(self.size)]
        self.flagged = [[False for _ in range(self.size)] for _ in range(self.size)]
        self.mines_count = sum(row.count("x") for row in self.grid)  # Count mines
        self.mode = False
        self.directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    def is_valid(self, x, y):
        return 0 <= x < self.size and 0 <= y < self.size
    
    def auto_reveal(self, x, y, auto_reveal_count):
        if not self.is_valid(x,y) or self.revealed[x][y] or self.flagged[x][y]:
            return
        zero_flag = False
        if self.grid[x][y] == 0:
            zero_flag = True
        queue = [(x,y)]
        
        while queue:
            if not zero_flag and auto_reveal_count < 1:
                break
            cx, cy = queue.pop(0)
            auto_reveal_count -= 1

            if not self.is_valid(cx,cy) or self.revealed[cx][cy] or self.grid[cx][cy] == 'x':
                continue

            self.revealed[cx][cy] = True

            if self.grid[cx][cy] == 0 or auto_reveal_count >= 1:
                for dx, dy in self.directions:
                    nx, ny = cx + dx, cy + dy
                    if self.is_valid(nx, ny) and not self.revealed[nx][ny] and self.grid[nx][ny] != 'x':
                        queue.append((nx, ny))


    def display(self):
        for x in range(self.size):
            for y in range(self.size):
                if self.revealed[x][y]:
                    print(self.grid[x][y], end = " ")
                elif self.flagged[x][y]:
                    print("@", end = " ")
                else:
                    print("*", end = " ")
            print()

    def cell_Status(self, mode, x, y):
        auto_reveal = random.randrange(0,(self.size//2)+2)
        print(auto_reveal)

        if mode:  # Flagging mode
            if not self.revealed[x][y]:
                self.flagged[x][y] = not self.flagged[x][y]
        else:  # Revealing mode
            if not self.flagged[x][y]:
                if self.grid[x][y] == 0 or auto_reveal > 0:
                    self.auto_reveal(x, y, auto_reveal)  # Auto-reveal connected empty spaces
                else:
                    self.revealed[x][y] = True  # Reveal single cell

    def ensure_safe_first_move(self, x, y):
        """Ensures the first move never lands on a mine."""
        if self.grid[x][y] == "x":
            # Find a non-mine cell and swap values
            for i in range(self.size):
                for j in range(self.size):
                    if self.grid[i][j] != "x":
                        self.grid[x][y], self.grid[i][j] = self.grid[i][j], "x"
            GridGenerator._calculate_adjacent_mines()
            GridGenerator.save_grid()