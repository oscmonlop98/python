from random import randrange

emptyCell = "empty"
discEne = ''


def myName():
    return "ANA"

def comprobarEne(grid:list, disc:str) -> int:

    global emptyCell
    global discEne

    #comprueba 3 enemigas seguidas
    for r in range(0,6):
        for c in range(0,9):
            if grid[r][c] == discEne:
                 #comprueba torre
                if r > 0 and r <=3:
                    if grid[r][c] == discEne and grid[r+1][c] == discEne and grid[r+2][c] == discEne and grid[r-1][c] == emptyCell:
                        return c

                #comprueba linea
                if c <= 6:
                    if grid[r][c+1] == discEne and grid[r][c+2] == discEne:
                        if c > 0:
                            if grid[r][c-1] == emptyCell:
                                if grid[r+1][c-1] == disc or grid[r+1][c-1] == discEne:
                                    return c-1
                        if c < 6:
                            if grid[r][c+3] == emptyCell:
                                if grid[r+1][c+3] == disc or grid[r+1][c+3] == discEne:
                                    return c+3
                            if grid[r][c+1] == emptyCell and grid[r][c+2] == discEne and grid[r][c+3] == discEne:
                                if r < 5:
                                    if grid[r+1][c+1] == disc or grid[r+1][c+1] == discEne:
                                        return c+1
                                return c+1
                            
                            if grid[r][c+1] == discEne and grid[r][c+2] == emptyCell and grid[r][c+3] == discEne:
                                if r < 5:
                                    if grid[r+1][c+2] == disc or grid[r+1][c+2] == discEne:
                                        print("AAAAAAAAAAAAA")
                                        return c+2
                                return c+2

    
                    
                        

    #comprueba diagonales ascendentesde fichas enemigas
    for r in range(0,6):
        for c in range(0,9):
            if grid[r][c] == discEne:

                #comprueba diagonales (ascendente)
                if c >= 3:
                    if grid[r+1][c-1] == discEne and grid[r+2][c-2] == discEne:
                        if r > 0:
                            if c < 8:
                                if grid[r-1][c+1] == emptyCell and grid[r][c+1] != emptyCell:
                                    return c+1
                        
                            if r == 1:
                                if grid[r+3][c-3] == emptyCell:
                                    if grid[r+4][c-3] != emptyCell:
                                        return c-3
                            if grid[r+3][c-3] == emptyCell:
                                return c-3
                        else:
                            if grid[r+3][c-3] == emptyCell and c>=3:
                                if grid[r+4][c-3] != emptyCell:
                                    return c-3

                #diagonales con huecos (ascendente)
                if c >= 3 and r < 3:
                    if grid[r+1][c-1] == discEne and grid[r+2][c-2] == emptyCell and grid[r+3][c-3] == discEne and grid[r+3][c-2] != emptyCell:
                        return c-2
                    if grid[r+1][c-1] == emptyCell and grid[r+2][c-2] == discEne and grid[r+3][c-3] == discEne and grid[r+3][c-1] != emptyCell:
                        return c-1

                #comprueba diagonales (descendente)
    for r in range(0,6):
        for c in range(0,9):
            if grid[r][c] == discEne:
                if c <= 5:
                    if grid[r+1][c+1] == discEne and grid[r+2][c+2] == discEne:
                        if r > 0:
                            if grid[r-1][c-1] == emptyCell and grid[r][c-1] != emptyCell:
                                return c-1
                            if r == 1:
                                if grid[r+3][c+3] == emptyCell and grid[r+4][c+3] != emptyCell:
                                    return c+3
                            if grid[r+3][c+3] == emptyCell:
                                return c+3
                        else:
                            if grid[r+3][c+3] == emptyCell and grid[r+4][c+3] != emptyCell and c<=5:
                                return c+3

                #diagonales con huecos (descendente)
                if c <= 5 and r < 3:
                    if grid[r+1][c+1] == discEne and grid[r+2][c+2] == emptyCell and grid[r+3][c+3] == discEne and grid[r+3][c+2] != emptyCell:
                        return c+2
                    if grid[r+1][c+1] == emptyCell and grid[r+2][c+2] == discEne and grid[r+3][c+3] == discEne and grid[r+3][c+1] != emptyCell:
                        return c+1

                
        
    
    #comprueba fichas enemigas continuas
    for r in range(0,6):
        for c in range(0,9):
            
            if grid[r][c] == discEne:

                #comprueba fila de fichas enemigas
                if c <= 6:                    
                    if grid[r][c+1] == discEne and grid[r][c+2] != discEne and grid[r][c+2] != disc:

                        if c == 6 and grid[0][c-1] == emptyCell:
                            return c-1

                        if c > 0:
                            if grid[r][c-1] == emptyCell:
                                return c-1
                            
                        if grid[0][c+2] == emptyCell:
                            return c+2
                    
                    if grid[r][c+1] == emptyCell and grid[r][c+2] == discEne:
                        if r<5:
                            if grid[r+1][c+1] == emptyCell and grid[0][c] == emptyCell:
                                return c
                        if grid[0][c+1] == emptyCell:
                            return c+1
                    
    return -1

def comprobar(grid:list, disc:str) -> int:

    global emptyCell
    global discEne

#comprueba si se puede ganar
    for r in range(0,6):
        for c in range(0,9):
            if grid[r][c] == disc:

                #comprueba torre
                if r > 0 and r <=3:
                    if grid[r][c] == disc and grid[r+1][c] == disc and grid[r+2][c] == disc and grid[r-1][c] == emptyCell:
                        return c

                #comprueba linea
                if c <= 6:
                    if grid[r][c+1] == disc and grid[r][c+2] == disc:
                        if c > 0:
                            if grid[r][c-1] == emptyCell:
                                if grid[r+1][c-1] != emptyCell:
                                    return c-1
                        if c < 6:
                            if grid[r][c+3] == emptyCell:
                                if grid[r+1][c+3] != emptyCell:
                                    return c+3
                            if grid[r][c+1] == emptyCell and grid[r][c+2] == disc and grid[r][c+3] == disc:
                                if r < 5:
                                    if grid[r+1][c+1] != emptyCell:
                                        return c+1
                                return c+1
                            
                            if grid[r][c+1] == disc and grid[r][c+2] == emptyCell and grid[r][c+3] == disc:
                                if r < 5:
                                    if grid[r+1][c+2] != emptyCell:
                                        return c+2
                                return c+2

    #comprueba diagonales 
    for r in range(0,6):
        for c in range(0,9):
            if grid[r][c] == disc:

                #comprueba diagonales (ascendente)
                if c >= 3:
                    if grid[r+1][c-1] == disc and grid[r+2][c-2] == disc:
                        if r > 0:
                            if c < 8:
                                if grid[r-1][c+1] == emptyCell and grid[r][c+1] != emptyCell:
                                    return c+1
                        
                            if r == 1:
                                if grid[r+3][c-3] == emptyCell:
                                    if grid[r+4][c-3] != emptyCell:
                                        return c-3
                            if grid[r+3][c-3] == emptyCell:
                                return c-3
                        else:
                            if grid[r+3][c-3] == emptyCell and c>=3:
                                if grid[r+4][c-3] != emptyCell:
                                    return c-3

                #diagonales con huecos (ascendente)
                if c >= 3 and r < 3:
                    if grid[r+1][c-1] == disc and grid[r+2][c-2] == emptyCell and grid[r+3][c-3] == disc and grid[r+3][c-2] != emptyCell:
                        return c-2
                    if grid[r+1][c-1] == emptyCell and grid[r+2][c-2] == disc and grid[r+3][c-3] == disc and grid[r+3][c-1] != emptyCell:
                        return c-1

                #comprueba diagonales (descendente)
                if c <= 5:
                    if grid[r+1][c+1] == disc and grid[r+2][c+2] == disc:
                        if r > 0:
                            if grid[r-1][c-1] == emptyCell and grid[r][c-1] != emptyCell:
                                return c+1
                            if r == 1:
                                if grid[r+3][c+3] == emptyCell and grid[r+4][c+3] != emptyCell:
                                    return c+3
                            if grid[r+3][c+3] == emptyCell:
                                return c+3
                        else:
                            if grid[r+3][c+3] == emptyCell and grid[r+4][c+3] != emptyCell and c<=5:
                                return c+3

                #diagonales con huecos (descendente)
                if c <= 5 and r < 3:
                    if grid[r+1][c+1] == disc and grid[r+2][c+2] == emptyCell and grid[r+3][c+3] == disc and grid[r+3][c+2] != emptyCell:
                        return c+2
                    if grid[r+1][c+1] == emptyCell and grid[r+2][c+2] == disc and grid[r+3][c+3] == disc and grid[r+3][c+1] != emptyCell:
                        return c+1
    return -1


def column(grid:list, disc:str) -> int:
    global emptyCell
    global discEne

    if discEne == '':
        if disc == "@":
            discEne = "#"
        else:
            discEne = "@"

    if emptyCell == "empty":
       emptyCell = grid[0][0]
    

    opcion = comprobar(grid,disc)
    if opcion >= 0 and grid[6][opcion] >= 0:
        return opcion
        
            
    opcion = comprobarEne(grid, disc)
    if opcion >= 0 and grid[6][opcion] >= 0:
        return opcion
    
    eleccion = 9

    while eleccion > 8:
        posibilidad = randrange(0,9,1)
        if grid[0][posibilidad] == emptyCell:
            eleccion = posibilidad

    return eleccion
