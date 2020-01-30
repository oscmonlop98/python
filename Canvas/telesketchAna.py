from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Telesketch")

lastx, lasty = 300, 300
nextx, nexty =  300,300


def setColor(newcolor):
    global color
    color = newcolor

def drawLeft():
    global nextx
    if nextx >= 10:
        nextx -= 10
        addLine()

def drawRight():
    global nextx
    if nextx < 600:
        nextx += 10
        addLine()

def drawUp():
    global nexty
    if nexty >= 10:
        nexty -= 10
        addLine()
        
def drawDown():
    global nexty
    if nexty < 600:
        nexty += 10
        addLine()
    
def addLine():
    global lastx, lasty, nextx, nexty
    drawingCanvas.create_line((lastx, lasty, nextx, nexty))
    lastx, lasty = nextx, nexty


window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)
window.update()

drawingCanvas = Canvas(window, borderwidth=10,relief="ridge")
drawingCanvas.config(width=600, height=600)
drawingCanvas.grid(column=0, row=0, sticky=(N, W, E, S))

controlCanvas = Canvas(window,  borderwidth=2,relief="sunken")
controlCanvas.config(width=600, height=100)
controlCanvas.grid(column=0, row=1, sticky=(N,W,E,S))

color = "black"

points = [30,50,60,30,60,70]
id = controlCanvas.create_polygon(points, outline='#f11',
    fill='#1f1', width=2)
controlCanvas.tag_bind(id, "<Button-1>", lambda x: drawLeft())

points = [70,30,100,50,70,70]
id = controlCanvas.create_polygon(points, outline='#f11',
    fill='#1f1', width=2)
controlCanvas.tag_bind(id, "<Button-1>", lambda x: drawRight())

points = [570,20,590,50,550,50]
id = controlCanvas.create_polygon(points, outline='#f11',
    fill='#1f1', width=2)
controlCanvas.tag_bind(id, "<Button-1>", lambda x: drawUp())

points = [550,60,590,60,570,90]
id = controlCanvas.create_polygon(points, outline='#f11',
    fill='#1f1', width=2)
controlCanvas.tag_bind(id, "<Button-1>", lambda x: drawDown())

window.mainloop()
