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


color = "red"


def setColor(newcolor):
    global color
    color = newcolor


root = Tk()
f = ttk.Frame()
f.pack()
cnv = Canvas(f, width=800, height=800)
cnv.grid(row=0, column=0)


circulo = [375,375,425,425]
id = cnv.create_oval(circulo, fill=color, width=3)
cnv.tag_bind(id, "<Button-1>", lambda x: setColor("black"))

ovalogrande = [780,780,30,30]
cnv.create_oval(ovalogrande, width=2)

ovalogrande2 = [790,790,20,20]
cnv.create_oval(ovalogrande2, width=3)
km = [400,470]

lineminutes = [402,402,302,140]
cnv.create_line(lineminutes, width=12)
lineseconds = [402,402,422,120]
cnv.create_line(lineseconds, fill='#3277D6', width=4)
linehours = [402,402,502,280]
cnv.create_line(linehours, width=12)

short = [[-350, 0],[-300, 0]]
homogenize(short)
toorig = gettranslation(400, 400)
for rot in range(0,360,6):
    rotation = getrotation(rot)
    transform = np.dot(rotation, toorig)
    temp = list()
    for i in range(len(short)):
        temp.append(np.dot(short[i],transform).tolist())
    dehomogenize(temp)
    ida = cnv.create_line(temp, fill=color)


large = [[-350, 0],[-300, 0]]
homogenize(large)
toorig = gettranslation(400, 400)
for rot in range(0,360,30):
    rotation = getrotation(rot)
    transform = np.dot(rotation, toorig)
    temp = list()
    for i in range(len(large)):
        temp.append(np.dot(large[i],transform).tolist())
    dehomogenize(temp)
    cnv.create_line(temp, width=4)

pos = [[-280, 0]]
homogenize(pos)
toorig = gettranslation(400, 400)
hour = 1
for rot in range(120,480,30):
    rotation = getrotation(rot)
    transform = np.dot(rotation, toorig)
    temp = list()
    temp.append(np.dot(pos[0],transform).tolist())
    dehomogenize(temp)
    cnv.create_text(temp, font="Times 15 italic bold", text=str(hour))
    hour = hour + 1


root.mainloop()