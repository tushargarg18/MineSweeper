from grid_generator import GridGenerator
from manual_solver import Manual_Solver
from auto_solver import Auto_Solver

if __name__ == "__main__":
    obj = GridGenerator(size=4, num_mines=4)
    obj.save_grid()
    
    auto_game = Auto_Solver()
    auto_game.solve()
    
    game = Manual_Solver()
    game.play()