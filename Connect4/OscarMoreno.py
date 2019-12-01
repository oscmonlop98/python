from random import randrange

inicio = 4
partidaEmpezada = 0
def myName():
    return "prueba"

def column(grid:list, disc:str) -> int:
    vacio = str(grid[0][0])
    botAliado = ''
    botEnemigo = ''
    ganarHD = 0
    ganarHI = 0
    perderHD = 0
    perderHI = 0
    ganarV = 0
    perderV = 0
    global inicio
    global partidaEmpezada

    # # Empezar siempre desde columna 4
    if inicio == 4 and grid[5][4] == vacio:
        inicio = 0
        return 4

    if partidaEmpezada == 0 and grid[5][4] == '@':
        botAliado = '@'
        botEnemigo = '#'
        variableAux = 1
    else:
        botAliado = '#'
        botEnemigo = '@'
        variableAux = 1

    # Tira cerca de cualquier ficha comprobando en vertical y horizontal
    for fila in range(0,6):
        for columna in range(0,8):
            # Comprobar si puedo ganar en horizontal hacia la derecha
            if grid[fila][columna] == botAliado and grid[fila][columna + 1] == botAliado and grid[fila][columna + 2] == botAliado and columna + 2 <= 8 and ganarHD == 0:
                ganarHD = 1
                return columna + 3
            # Comprobar si puedo ganar en horizontal hacia la izquierda
            elif grid[fila][columna] == botAliado and grid[fila][columna - 1] == botAliado and grid[fila][columna - 2] == botAliado and columna - 2 <= 0 and ganarHI == 0:
                ganarHI = 1
                return columna -3
            # Comprobar si puedo ganar en vertical
            elif grid[fila][columna] == botAliado and grid[fila+1][columna] == botAliado and grid[fila+2][columna] == botAliado and ganarV == 0:
                if grid[6][columna] > 0:
                    ganarV = 1
                    return columna
            # Comprobar si el enemigo gana en vertical
            elif grid[fila][columna] == botEnemigo and grid[fila+1][columna] == botEnemigo and grid[fila+2][columna] == botEnemigo and perderV == 0:
                if grid[6][columna] > 0:
                    perderV = 1
                    return columna
            # Comprobar si el enemigo gana en horizontal hacia la derecha
            elif grid[fila][columna] == botEnemigo and grid[fila][columna+1] == botEnemigo and grid[fila][columna+2] == botEnemigo and columna + 2 <= 8 and perderHD == 0:
                perderHD = 1
                return columna + 3
            # Comprobar si el enemigo gana en horizontal hacia la izquierda
            elif grid[fila][columna] == botEnemigo and grid[fila][columna-1] == botEnemigo and grid[fila][columna-2] == botEnemigo and columna - 2 <= 0 and perderHI == 0:
                perderHI = 1
                return columna - 3
            elif grid[fila][columna] == botEnemigo:
                if columna == 0 and grid[6][columna] > 0:
                    return columna
                elif grid[6][columna+1] > 0:
                    return columna+1
                elif columna == 8 and grid[6][columna] > 0:
                    return columna
                elif grid[6][columna-1] > 0:
                    return columna-1
                elif grid[6][columna] > 0:
                    return randrange(0, 9, 1)

    # for fila in range(0,6):
    #     for columna in range(0,8):
    #         while grid[6][columna] > 0:
    #             return randrange(3,5,1)

    return randrange(0,9,1)