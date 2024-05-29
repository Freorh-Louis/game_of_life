
def download(file):
    f = open(file, 'r')
    L = f.readlines()
    lines = []
    inline = ''
    for line in L:
        if line[0] == '#':
            continue
        elif line[0] == 'x':
            param = line.split(',')
            param = param[0] + param[1]
            coord = [int(e) for e in param.split() if e.isdigit()]
        else:
            for e in line.split('$'):
                if e[-1] == '\n':
                    e = e[:-1]
                    inline = e
                else:
                    lines.append(inline + e)
                    inline = ''
                
    
    tab = [[False for i in range(coord[0])] for j in range(coord[1])]
    print(lines)
    for i in range(len(lines)):
        file_pos = 0
        tab_pos = 0
        while file_pos < len(lines[i]):
            nbr = ''
            while lines[i][file_pos].isnumeric():
                nbr += lines[i][file_pos]
                file_pos += 1
            
            if nbr == '':
                if lines[i][file_pos] == 'o':
                    tab[i][tab_pos] = True
            else:
                for j in range(int(nbr)):
                    if lines[i][file_pos] == 'o':
                        tab[i][tab_pos + j] = True
                tab_pos += int(nbr) - 1
            
            file_pos += 1
            tab_pos += 1

    return tab, coord[0], coord[1]


def upload(pattern, height, width, file_name):
    pattern_str = ""
    for i in range(height):
        cpt = 0
        for j in range(width):
            if pattern[i][j]:
                cpt += 1
                if j < width-1 and pattern[i][j+1]:
                    continue
                else:
                    if cpt == 1:
                        pattern_str += "o"
                    else:
                        pattern_str += str(cpt) + "o"
                    cpt = 0
            else:
                cpt += 1
                if j < width-1 and not pattern[i][j+1]:
                    continue
                else:
                    if cpt == 1:
                        pattern_str += "b"
                    else:
                        pattern_str += str(cpt) + "b"
                    cpt = 0
        pattern_str += "$"
    
    pattern_str = pattern_str[:-1]
    pattern_str += "!"
    str_list = []
    if len(pattern_str) > 70:
        str_list  = [pattern_str[:70*(i+1)] for i in range(int(len(pattern_str)/70) + 1)]
    print(str_list)

    text = f"# {file_name}\n# Louis VINCENT\nx = {width}, y = {height}, rule = B3/S23\n" + pattern_str
    print(text)

    """ file = open(file_name + ".rle.txt", "x")
    file.write(text)
    file.close() """


pattern, width, height = download("gosperglidergun.rle.txt")
upload(pattern, height, width, "test")