# Ejercicio1
def cartProd(A: set, B: set):

    num = len(A+B)
    axb = set()

    for i in range(num):
        pos1 = (A[i],B[i])
        pos2 = (A[i],B[i+1])
        axb.add((pos1,pos2))
    return(axb)


K = ['a','b']
U = ['c','d']
print("Ejercicio 1")
# print(cartProd(K,U))

# Ejercicio2
def delDups(L):
    elem_set = set()
    dups_set = set()

    for entry in L:
        len_initial = len(elem_set)
        elem_set.add(entry)
        len_after = len(elem_set)
        if len_initial == len_after:
            dups_set.add(entry)
    return (elem_set)
aa = [1, 1, 2, 3, 4, 2]
print("Ejercicio 2")
print(delDups(aa))

# Ejercicio3
def getClear(dict1):

    dict1 = {}
    dict2 = {}
    aux = 96
    for i in range(26):
        aux = aux +1
        letra = chr(aux)
        dict1 = {letra:letra}
        dict2.update(dict1)
    return dict2
abc = {}
print("Ejercicio 3")
print(getClear(abc))

# Ejercicio4
import random

def shuffleDict(a):

    dict1 = {}
    dict2 = {}
    aux = 96
    aux2 = []
    for i in range(26):
        aux = aux +1
        letra = chr(aux)
        dict1 = {letra:letra}
        dict2.update(dict1)
        aux2 += letra
    aux2 = random.shuffle(aux2)

    return dict2

aa = {}
print("Ejercicio 4")
print(shuffleDict(aa))