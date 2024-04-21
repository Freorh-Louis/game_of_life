import tkinter as tk

class Grid:

    def __init__(self, game):
        self.__grid = [[False]*110]*90
        self.__next_grid = [[False]*110]*90
        self.__entity_grid = [[False]*110]*90
        self.__game = game
    
    def birth(self, x, y):
        self.__next_grid[x][y] = True
        self.__entity_grid[x][y] = self.__game.create_rectangle(x*10, y*10, x*10 + 10, y*10 + 10, fill = "white", outline = "black")
    
    def death(self, x, y):
        self.__next_grid[x][y] = False
        self.__game.delete(self.__entity_grid[x][y])

    def update_grid(self):
        self.__grid = self.__next_grid
    