from download_upload import download

class Copy_paste:

    def __init__(self, grid, pause, paste_file):
        self.__grid = grid
        self.__pause = pause
        self.__paste_file = paste_file

    def paste(self):
        if self.__pause.get():
            widget_txt = self.__paste_file.get('1.0', 'end-1c').split(',')
            file = widget_txt[0]
            x = int(widget_txt[1])
            y = int(widget_txt[2])
            pattern, width, height = download(file)
            current_grid = self.__grid.get_grid()
            if x + width > 110 and y + height > 90:
                print('Pattern does not fit in the screen')
            else:
                for i in range(height):
                    for j in range(width):
                        if pattern[i][j]:
                            if not current_grid[i + x][j + y]:
                                self.__grid.birth(i + x, j + y)
                        else:
                            if current_grid[i + x][j + y]:
                                self.__grid.death(i + x, j + y)
                self.__grid.update_grid()