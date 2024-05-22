import tkinter as tk
from grid import Grid
from game_states import Game_states
from copy_paste import Copy_paste

window = tk.Tk()
window.title("The game of life")
window.geometry("1400x900")

game = tk.Canvas(window, width = "1100", height = "900", bg = "black")
speed = tk.Scale(window, label = "Choose the speed", from_ = 1, to = 1000)
paste_file = tk.Text(window, height = 1, width = 37)
paste_label = tk.Label(window, text = "Paste a pattern file : filename.rle.txt,x,y")

pause = tk.BooleanVar()
pause.set(True)

new_board = Grid(game)
states = Game_states(game, new_board, speed, pause)
copy_paste_class = Copy_paste(new_board, pause, paste_file)

quit_game = tk.Button(window, text = "Quit game", command = window.destroy)
pause_button = tk.Button(window, text = "Start/Stop", command = states.pause_function)
reset = tk.Button(window, text = "Reset", command = states.reset_function)
paste_button = tk.Button(window, text = "Paste your pattern", command = copy_paste_class.paste)

game.grid(row = 1, column = 1, rowspan = 5)
pause_button.grid(row = 1, column = 2)
reset.grid(row = 2, column = 2)
speed.grid(row = 3, column = 2)
paste_label.grid(row = 4, column = 2, sticky = "N")
paste_file.grid(row = 4, column = 2)
paste_button.grid(row = 4, column = 2, sticky = "S")
quit_game.grid(row = 5, column = 2)


states.generation()
game.bind("<Button-1>", states.place_function)
game.bind("<Button-3>", states.remove_function)


window.mainloop()