import os

class Generation:

    def __init__(self, game, grid):
        self.__game = game
        self.__grid = grid


    def count_neighbours(self, current_grid, x, y):
        alive = 0
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if i > 0 and i < 110 and j > 0 and j < 90 and (i,j) != (x,y) and current_grid[i][j]:
                    alive +=1
                    
        return alive


    def generation(self):
        current_grid = self.__grid.get_grid()

        for i in range(110):
            for j in range(90):
                alive = self.count_neighbours(current_grid, i, j)

                if (alive < 2 or alive > 3) and current_grid[i][j]:
                    self.__grid.death(i, j)
                elif alive == 3 and not current_grid[i][j]:
                    self.__grid.birth(i, j)
            
        self.__grid.update_grid()
        self.__game.after(int(os.environ["game_of_life_speed"]), self.generation)

