from tkinter import *
from tkinter import ttk
import numpy as np


def homogenize(coords: list)-> list:
    for i in range(len(coords)):
        coords[i].append(1)


def dehomogenize(coords: list):
    for i in range(len(coords)):
        coords[i][0] = coords[i][0] / coords[i][2]
        coords[i][1] = coords[i][1] / coords[i][2]
        del coords[i][2]


def gettranslation(tx:float, ty:float):
    return [[1, 0, 0], [0, 1, 0], [tx, ty, 1]]


def getrotation(deg: float)-> list:
    rad = np.radians(deg)
    return [[np.cos(rad), np.sin(rad), 0], [-np.sin(rad), np.cos(rad), 0], [0, 0, 1]]


root = Tk()

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

drawingCanvas = Canvas(root, borderwidth=10,relief="ridge")
drawingCanvas.config(width=600, height=600)
drawingCanvas.grid(column=0, row=0, sticky=(N, W, E, S))

triangle = [[120,200], [240,120], [240,280]]
id = drawingCanvas.create_polygon(triangle, outline='#f11', fill='#1f1', width=2)

homogenize(triangle)
mat = gettranslation(0,0)
a = np.array(mat)
b = np.array(triangle)
c = np.array(b.dot(a))
x = c.tolist()

matr = getrotation(25)
a = np.array(matr)
b = np.array(triangle)
c = np.array(b.dot(a))
x = c.tolist()

matb = gettranslation(80,80)
a = np.array(matb)
b = np.array(triangle)
c = np.array(b.dot(a))
x = c.tolist()
dehomogenize(x)

id = drawingCanvas.create_polygon(x, outline='#f11', fill='#1f1', width=2)

root.mainloop()

