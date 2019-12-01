from random import randrange

inicio = 4;
def myName():
    return "REY"
def column(grid:list, disc:str) -> int:

    bot1 = '@'
    bot2 = '#'
    for i in range(1, 9):
        if str(grid[i][6]) != 0:
            if str(grid[0][4]) != bot1 != bot2:
                return inicio;
        return randrange(0, 9, 1)