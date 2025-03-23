from grid_generator import GridGenerator
from manual_solver import Manual_Solver

if __name__ == "__main__":
    obj = GridGenerator(size=4, num_mines=4)
    obj.save_grid()
    game = Manual_Solver()
    game.play()