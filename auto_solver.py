from game_logic import Game_Logic
import json
from heapq import heappush, heappop
import time

class Auto_Solver(Game_Logic):
    def __init__(self, file_name = "grid.json"):
        with open(file_name, "r") as f:
            data = json.load(f)
        self.size = data["size"]
        self.grid = data["grid"]
        self.revealed = [[False for _ in range(self.size)] for _ in range(self.size)]
        self.flagged = [[False for _ in range(self.size)] for _ in range(self.size)]
        self.directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    
    def reveal_cells_regressively(self, x, y):
        queue = []
        heappush(queue, (self.grid[x][y], x, y))  # Use heap to prioritize lowest numbers
        while queue:
            _, cx, cy = heappop(queue)  # Pick the lowest-risk cell
            if self.revealed[cx][cy]:  
                continue  # Skip if already revealed
            
            self.revealed[cx][cy] = True
            Game_Logic.display(self)
            print("\n")

            if self.grid[cx][cy] == 0:
                # If it's a zero, expand to all neighbors
                for dx, dy in self.directions:
                    nx, ny = cx + dx, cy + dy
                    if self.is_valid(nx, ny) and not self.revealed[nx][ny]:
                        heappush(queue, (self.grid[nx][ny], nx, ny))
            else:
                # If it's not zero, still add adjacent safe cells to the queue
                for dx, dy in self.directions:
                    nx, ny = cx + dx, cy + dy
                    if self.is_valid(nx, ny) and not self.revealed[nx][ny] and self.grid[nx][ny] != "x":
                        heappush(queue, (self.grid[nx][ny], nx, ny))

    def solve(self):
        """Main solver function that starts from the first revealed cell."""
        start_time = time.time()
        self.reveal_cells_regressively(0, 0)  # Start from user’s first move
        end_time = time.time()
        print(f"Solver completed in {end_time - start_time:.5f} seconds")

    