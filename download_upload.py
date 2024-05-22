
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