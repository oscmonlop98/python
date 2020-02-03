from tkinter import *
from tkinter import ttk
import numpy as np


def homogenize(coords: list):
    for i in range(len(coords)):
        coords[i].append(1)
    return coords


def dehomogenize(coords: list):
    for i in range(len(coords)):
        coords[i][0] = coords[i][0] / coords[i][2]
        coords[i][1] = coords[i][1] / coords[i][2]
        del coords[i][2]


def gettranslation(tx:float, ty:float)->list:
    return [[1, 0, 0], [0, 1, 0], [tx, ty, 1]]


def getrotation(deg:float)->list:
    rad = np.radians(deg)
    return [[np.cos(rad), np.sin(rad), 0], [-np.sin(rad), np.cos(rad), 0], [0, 0, 1]]


root = Tk()
f = ttk.Frame()
f.pack()
cnv = Canvas(f, width=800, height=800)
cnv.grid(row=0, column=0)

# Círculo central
ovalo = [360,360,420,420]
cnv.create_oval(ovalo, fill='#f11', width=4)

# Líneas velocímetro
linea = [[-350, 0],[-300, 0]]
homogenize(linea)
# Le pasamos los puntos de la línea respecto al origen de coordenadas respectivamente corresponden a 'x' e 'y'
toorig = gettranslation(400, 400)
for rot in range(-20,220,20):
    rotation = getrotation(rot)
    transform = np.dot(rotation, toorig)
    linea2 = list()
    for z in range(len(linea)):
        linea2.append(np.dot(linea[z], transform).tolist())
    dehomogenize(linea2)
    print(linea2)
    cnv.create_line(linea2, width=2)

large = [[-350, 0],[-280, 0]]
homogenize(large)
toorig = gettranslation(400, 400)
for rot in range(-30,220,20):
    rotation = getrotation(rot)
    transform = np.dot(rotation, toorig)
    temp = list()
    for i in range(len(linea)):
        temp.append(np.dot(large[i],transform).tolist())
    dehomogenize(temp)
    cnv.create_line(temp, width=3)

needle = [[0,0], [-7, -7], [0, -150], [7, -7]]
homogenize(needle)
toorig = gettranslation(400, 400)
needle2 = list()
for i in range(len(needle)):
    needle2.append(np.dot(needle[i],toorig).tolist())
dehomogenize(needle2)
cnv.create_polygon(needle2, outline='#f11', fill='#1f1', width=3)

# marca = [[350, 0],[290, 0]]
# cnv.create_line(marca, width=3)


root.mainloop()