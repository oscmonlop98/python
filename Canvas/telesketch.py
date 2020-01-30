from tkinter import *
from tkinter import ttk

lastx, lasty = 300,200
nextx, nexty = 300,200

color = "black"
def setColor(newcolor):
    global color
    color = newcolor

def xy(event):
    global lastx, lasty
    lastx, lasty = event.x, event.y


def onObjectClick():
    global nextx
    if nextx >= 10:
        nextx -= 10
        addLine()

def addLine():
    global lastx, lasty, nextx, nexty
    canvas.create_line((lastx, lasty, nextx, nexty))
    lastx, lasty = nextx, nexty




root = Tk()
root.title("TeleSketch")
root.geometry("600x400")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

mainframe = ttk.Frame(root)
mainframe.configure(relief='ridge', padding=10)
mainframe.grid(row=0, column=0)

canvas = Canvas(mainframe, height=300, width=500)
canvas.grid(column=0, row=0, sticky=(N, W, E, S))
canvas.bind("<Button-1>", xy)
canvas.bind("<B1-Motion>", addLine)


# canvas.tag_bind(id, "<Button-1>", lambda x: setColor("red"))
# id = canvas.create_rectangle((10, 35, 30, 55), fill="blue")
# canvas.tag_bind(id, "<Button-1>", lambda x: setColor("blue"))
# id = canvas.create_rectangle((10, 60, 30, 80), fill="black")
# canvas.tag_bind(id, "<Button-1>", lambda x: setColor("black"))


controlframe = ttk.Frame(root)
controlframe.configure(relief='raised', padding=10)
controlframe.grid(row=1, column=0)

canvas2 = Canvas(controlframe, height=40, width=500)
canvas2.grid(column=0, row=0, sticky=(N, W, E, S))


pointsleft = [40,1, 40, 40, 15,23, 40,1]
id = canvas2.create_polygon(pointsleft, outline='#f11', fill='#1f1', width=2)

canvas2.tag_bind(id, '<ButtonPress-1>', lambda x: onObjectClick())

pointsright = [46,1, 46,40, 70,23, 46,1]
canvas2.create_polygon(pointsright, outline='#f11', fill='#1f1', width=2)

pointsup = [451,21, 481,21, 465,1, 451,21]
canvas2.create_polygon(pointsup, outline='#f11', fill='#1f1', width=2)

pointsdown = [451,20, 481,20, 465,40, 451,20]
canvas2.create_polygon(pointsdown, outline='#f11', fill='#1f1', width=2)


root.mainloop()