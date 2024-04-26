
class Game_states:

    def __init__(self, game, grid, speed, pause):
        self.__game = game
        self.__grid = grid
        self.__speed = speed
        self.__pause = pause


    def count_neighbours(self, current_grid, x, y):
        alive = 0
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if i > 0 and i < 110 and j > 0 and j < 90 and (i,j) != (x,y) and current_grid[i][j]:
                    alive +=1
                    
        return alive


    def generation(self):
        if not self.__pause.get():
            current_grid = self.__grid.get_grid()

            for i in range(110):
                for j in range(90):
                    alive = self.count_neighbours(current_grid, i, j)

                    if (alive < 2 or alive > 3) and current_grid[i][j]:
                        self.__grid.death(i, j)
                    elif alive == 3 and not current_grid[i][j]:
                        self.__grid.birth(i, j)
                
            self.__grid.update_grid()
            self.__game.after(self.__speed.get(), self.generation)
        else:
            self.__game.after(self.__speed.get(), self.generation)

    
    def pause_function(self):
        self.__pause.set(not self.__pause.get())
    
    
    def reset_function(self):
        current_grid = self.__grid.get_grid()

        for i in range(110):
                for j in range(90):
                    if current_grid[i][j]:
                          self.__grid.death(i, j)
        
        self.__grid.update_grid()
        self.__pause.set(True)
    

    def place_function(self, event):
        if self.__pause.get():
            x = int(event.x/10)
            y = int(event.y/10)
            current_grid = self.__grid.get_grid()

            if not current_grid[x][y]:
                self.__grid.birth(x, y)
            
            self.__grid.update_grid()
    

    def remove_function(self, event):
        if self.__pause.get():
            x = int(event.x/10)
            y = int(event.y/10)
            current_grid = self.__grid.get_grid()

            if current_grid[x][y]:
                self.__grid.death(x, y)
            
            self.__grid.update_grid()