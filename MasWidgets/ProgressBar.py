from tkinter import *
from tkinter import ttk
import random
from tkinter import colorchooser


def changeColor(wid):
    color = colorchooser.askcolor()
    locuraTotal(wid, color[1])


def locuraTotal(widget, color):
    a = []
    aux=0
    while len(a) < 250:
        codigo.set("Comprobando...")
        num = random.randint(0, 249)
        p['value'] = len(a)
        p.update()
        if (num in a):
            for i in range(1,100000):
                pass
        else:
            a.append(num)
            media = 100 / 250
            aux = aux + media
            porcentaje.set(str("%.2f" % aux) + "%")
            print(len(a))

    p.stop()
    widget['background'] = color
    codigo.set("A")
    # gui_style.configure("M.TFrame", background='red')


root = Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

gui_style = ttk.Style()
mainframe = ttk.Frame(root, style="M.TFrame")
mainframe['padding'] = (10, 10, 10, 10)
mainframe = ttk.Frame(root,relief='raised')
mainframe.grid()

porcentaje = StringVar()
porcentaje.set("0%")
p = ttk.Progressbar(mainframe, orient=HORIZONTAL, length=200, maximum=250, mode='determinate',
                    style="red.Horizontal.TProgressbar")
p.grid(column=0, row=1)

lbl = ttk.Label(mainframe, textvariable=porcentaje)
lbl.grid(row=2, column=0)

codigo = StringVar()
codigo.set('')
labelColor = ttk.Label(mainframe, relief='raised', textvariable=codigo)
labelColor['padding'] = (50,50)
labelColor.configure(anchor=CENTER)
labelColor.grid(row=0, column=0, sticky='nwse')

b = ttk.Button(mainframe, text="Click me", command=lambda: changeColor(labelColor))
b.grid(row=3, column=0)

s = ttk.Style()
s.configure("red.Horizontal.TProgressbar", foreground='red', background='red')
tema = StringVar()
combo = ttk.Combobox(mainframe, textvariable=tema)
combo['values'] = s.theme_names()
combo.bind('<<ComboboxSelected>>', lambda e: s.theme_use(tema.get()))
combo.grid(row=4, column=0,  sticky='nwse')

root.update()
root.minsize(root.winfo_width(), root.winfo_height())
mainframe.mainloop()
