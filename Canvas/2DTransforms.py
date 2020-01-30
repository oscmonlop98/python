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

# def crearLineas():

triangle = [[25, 50], [60, 75], [60, 25]]

root = Tk()
f = ttk.Frame()
f.pack()
cnv = Canvas(f, width=400, height=400)
cnv.grid(row=0, column=0)
cnv.create_polygon(triangle, outline='#f11', fill='#1f1', width=2)

homogenize(triangle)
triangle2 = list()
toorig = gettranslation(-48, -50)
topos = gettranslation(120, 50)
rotation = getrotation(180)
transform = np.dot(toorig, rotation)
transform = np.dot(transform, topos)
for i in range(len(triangle)):
    triangle2.append(np.dot(triangle[i],transform).tolist())
dehomogenize(triangle2)

cnv.create_polygon(triangle2, outline='#f11', fill='#1f1', width=2)

# Círculo central
ovalo = [180,180,210,210]
cnv.create_oval(ovalo, fill='#f11', width=4)

# Líneas velocímetro
linea = [[15, 195], [45, 195]]
cnv.create_line(linea, width=3)

homogenize(linea)
toorig = gettranslation(-195, -165)

for rot in range(0, 220, 20):
    rotation = getrotation(rot)
    transform = np.dot(rotation, toorig)
    temp = list()
    for i in range(len(linea)):
        temp.append((np.dot(linea[rot], transform).tolist()))
    dehomogenize(linea)
    cnv.create_line(temp, width=2)




root.mainloop()