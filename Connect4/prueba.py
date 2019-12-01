from random import randrange

inicio = 4
def myName():
    return "prueba"

def compruebaTirada(grid:list) -> int:
    for columna in range(0,9):
        for valor in grid[6][columna]:
            if valor > 0:
                return columna
            else:
                columna = columna + 1


def column(grid:list, disc:str) -> int:
    vacio = str(grid[0][4])
    bot1 = '@'
    bot2 = '#'
    global inicio

    # Empezar siempre desde columna 4
    if inicio == 4:
        inicio = 0
        return 4
    for columna in range(0,9):
        if columna

    # cont = 0
    #
    # for fil in range(0,6):
    #     for col in range(0,9):
    #         if grid[fil][col] == vacio or grid[fil][col] == bot1:
    #             cont = cont + 1;
    #         if cont <=3:
    #             return col



        # elif z == bot2:
        #     col = col+1
        #     cont = cont+1
        #     if cont > 1 and grid[6][col] > 0:
        #         return col + 1
        # return 4+1




    #     if cont <=3:
    #             if z == bot1:
    #                 col = col+1
    #                 cont = cont+1
    #             else:
    #                 col = col+1
    #     if grid[fil][col] != vacio != bot2:
    #         return col+1
    #     else:
    #         fil = fil+1
    # if grid[fil][col] != vacio != bot2:
    #     return 4







# for i in range(0,9):
#     while pos < len(grid[i][z]) and not encontrado:
#         if grid[pos] == item:
#             encontrado = True
#         else:
#             pos = pos+1


    # return randrange(0,9,1)
    # for i in range(1, 9):
    #     if str(grid[i][6]) != 0:
    #
    #     return randrange(0, 9, 1)