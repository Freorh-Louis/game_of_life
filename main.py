import tkinter as tk
from grid import Grid

window = tk.Tk()
window.title("The game of life")
window.geometry("1200x900")

game = tk.Canvas(window, width = "1100", height = "900", bg = "black")
quit_game = tk.Button(window, text = "Quit game", command = window.destroy)
restart = tk.Button(window, text = "Restart", command = None)

game.grid(row = 1, column = 1, rowspan = 2)
restart.grid(row = 1, column = 2)
quit_game.grid(row = 2, column = 2)

grid = Grid(game)



window.mainloop()