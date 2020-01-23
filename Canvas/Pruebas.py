# from tkinter import *
# from tkinter import ttk
#
# lastx, lasty = 0, 0
#
# color = "black"
# def setColor(newcolor):
#     global color
#     color = newcolor
#
# def xy(event):
#     global lastx, lasty
#     lastx, lasty = event.x, event.y
#
# def addLine(event):
#     global lastx, lasty
#     canvas.create_line((lastx, lasty, event.x, event.y), fill=color)
#     lastx, lasty = event.x, event.y
#
#
# root = Tk()
# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)
#
# canvas = Canvas(root)
# canvas.grid(column=0, row=0, sticky=(N, W, E, S))
# canvas.bind("<Button-1>", xy)
# canvas.bind("<B1-Motion>", addLine)
#
# id = canvas.create_rectangle((10, 10, 30, 30), fill="red")
# canvas.tag_bind(id, "<Button-1>", lambda x: setColor("red"))
# id = canvas.create_rectangle((10, 35, 30, 55), fill="blue")
# canvas.tag_bind(id, "<Button-1>", lambda x: setColor("blue"))
# id = canvas.create_rectangle((10, 60, 30, 80), fill="black")
# canvas.tag_bind(id, "<Button-1>", lambda x: setColor("black"))
#
# root.mainloop()

from tkinter import *

def onObjectClick(event):
    print('Got object click', event.x, event.y)
    print(event.widget.find_closest(event.x, event.y))

root = Tk()
canv = Canvas(root, width=100, height=100)
obj1Id = canv.create_line(0, 30, 100, 30, width=5)
obj2Id = canv.create_text(50, 70, text='Click', tags='obj2Tag')

canv.tag_bind(obj1Id, '<ButtonPress-1>', onObjectClick)
canv.tag_bind('obj2Tag', '<ButtonPress-1>', onObjectClick)
print('obj1Id: ', obj1Id)
print('obj2Id: ', obj2Id)
canv.pack()
root.mainloop()