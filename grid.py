import copy

class Grid:

    def __init__(self, game):
        self.__grid = [[False for i in range(90)] for j in range(110)]
        self.__next_grid = [[False for i in range(90)] for j in range(110)]
        self.__entity_tab = {}
        self.__game = game
    
    def birth(self, x, y):
        self.__next_grid[x][y] = True
        key = x*110 + y
        self.__entity_tab[key] = self.__game.create_rectangle(x*10, y*10, x*10 + 10, y*10 + 10, fill = "white", outline = "black")
    
    def death(self, x, y):
        self.__next_grid[x][y] = False
        key = x*110 + y
        self.__game.delete(self.__entity_tab[key])
        self.__entity_tab.pop(key)

    def get_grid(self):
        return self.__grid
    
    
    def update_grid(self):
        self.__grid = copy.deepcopy(self.__next_grid)
    