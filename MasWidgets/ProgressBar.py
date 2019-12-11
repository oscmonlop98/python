from tkinter import *
from tkinter import ttk
import random


def locuraTotal():
    a = []
    while len(a) < 250:
        num = random.randint(0, 249)
        p['value'] = len(a)
        p.update()
        if (num in a):
            for i in range(1,1000000):
                pass
        else:
            a.append(num)
            porcentaje.set(str(len(a)) + "%")
            print(len(a))

    p.stop()
    gui_style.configure("M.TFrame", background='red')


root = Tk()

gui_style = ttk.Style()
mainframe = ttk.Frame(root, style="M.TFrame")
mainframe.grid()

porcentaje = StringVar()
porcentaje.set("0%")
p = ttk.Progressbar(mainframe, orient=HORIZONTAL, length=200, maximum=250, mode='determinate')
p.grid(column=0, row=0)

lbl = ttk.Label(mainframe, textvariable=porcentaje)
lbl.grid(row=1, column=0)

b = ttk.Button(mainframe, text="A pastar", command=lambda: locuraTotal())
b.grid(row=2, column=0)

mainframe.mainloop()
