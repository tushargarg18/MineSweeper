import json
import random
from game_logic import Game_Logic
import time

class Manual_Solver(Game_Logic):

    def play(self):
        print("Minesweeper Started, Please enter coordinates as X,Y to proceed!")
        while True:
            start_time = time.time()
            Game_Logic.display(self)
            try:
                row, col = map(int, input("Enter Row and Column:").split())
                mode = input("Enter The mode - False to reveal, True to flag: ").strip().lower() == 'true'
            except ValueError:
                print("Invalid input, please enter a valid coordinate.")
                continue

            if self.grid[row][col] == "x" and not mode:
                print("Boom you hit a mine!! GAME OVER :)")
                print(self.grid)
                end_time = time.time()
                print(f"Manual solver completed in {end_time - start_time:.5f} seconds")
                break

            Game_Logic.cell_Status(self, mode, row, col)


            # Check if all non-mine cells are revealed and all mines are flagged
            if all(self.revealed[x][y] or self.flagged[x][y] for x in range(self.size) for y in range(self.size)) or \
               sum(self.flagged[x][y] for x in range(self.size) for y in range(self.size)) == self.mines_count:
                print("You Won !!!")
                end_time = time.time()
                print(f"Manual solver completed in {end_time - start_time:.5f} seconds")
                break