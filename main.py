import tkinter as tk
from grid import Grid
from game_states import Game_states

window = tk.Tk()
window.title("The game of life")
window.geometry("1300x900")

game = tk.Canvas(window, width = "1100", height = "900", bg = "black")
speed = tk.Scale(window, label = "Choose the speed", from_ = 1, to = 1000)

pause = tk.BooleanVar()
pause.set(True)

new_board = Grid(game)
states = Game_states(game, new_board, speed, pause)

quit_game = tk.Button(window, text = "Quit game", command = window.destroy)
pause_button = tk.Button(window, text = "Start/Stop", command = states.pause_function)
reset = tk.Button(window, text = "Reset", command = states.reset_function)

game.grid(row = 1, column = 1, rowspan = 4)
pause_button.grid(row = 1, column = 2)
reset.grid(row = 2, column = 2)
speed.grid(row = 3, column = 2)
quit_game.grid(row = 4, column = 2)


states.generation()
window.bind("<Button-1>", states.place_function)
window.bind("<Button-3>", states.remove_function)


window.mainloop()