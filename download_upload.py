
def download(file):
    f = open(file, 'r')
    L = f.readlines()
    lines = []
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
                lines.append(e)
                
    
    tab = [[False for i in range(coord[0])] for j in range(coord[1])]
    print(lines)
    for i in range(len(lines)):
        w = 0
        line_pos = 0
        while w < len(lines[i]):
            nbr = ''
            while lines[i][w].isnumeric():
                nbr += lines[i][w]
                w += 1
            
            if nbr == '':
                if lines[i][w] == 'o':
                    tab[i][line_pos] = True
            else:
                for j in range(int(nbr)):
                    if nbr == '2':
                        print('test : ', line_pos - len(nbr) + j)
                    if lines[i][w] == 'o':
                        tab[i][line_pos - len(nbr) + j] = True
                line_pos += int(nbr) - 1
            
            w += 1
            line_pos += 1
        print(line_pos)
        
    print(tab)

        
download('glider.rle.txt')
download('gosperglidergun.rle.txt')