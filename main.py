import tkinter as tk
import os
from generation import Generation
from grid import Grid

window = tk.Tk()
window.title("The game of life")
window.geometry("1300x900")

def test(a = 0):
    os.environ["game_of_life_speed"] = str(speed.get())

game = tk.Canvas(window, width = "1100", height = "900", bg = "black")
quit_game = tk.Button(window, text = "Quit game", command = window.destroy)
pause = tk.Button(window, text = "Start", command = None)
speed = tk.Scale(window, label = "Choose the speed", from_ = 1, to = 1000, command = test)

game.grid(row = 1, column = 1, rowspan = 3)
pause.grid(row = 1, column = 2)
speed.grid(row = 2, column = 2)
quit_game.grid(row = 3, column = 2)

new_board = Grid(game)
new_board.birth(49,50)
new_board.birth(50,51)
new_board.birth(50,52)
new_board.birth(51,51)
new_board.birth(49,52)
new_board.update_grid()

os.environ["game_of_life_speed"] = str(speed.get())

new_generation = Generation(game, new_board)
new_generation.generation()



window.mainloop()