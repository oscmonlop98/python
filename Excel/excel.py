from tkinter import *
from tkinter import ttk


def changeColor(widget):
    # x, y = widget.winfo_pointerxy()
    widget['background'] = 'red'


root = Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

mainframe = ttk.Frame(root)
mainframe.grid(column=0, row=0, sticky='nwse')

for i in range(1,5):
    mainframe.columnconfigure(i, weight=1, minsize='75p')
    mainframe.rowconfigure(i, weight=1, minsize='20p')

#LabelTop
letra = 65
for i in range(4):
    labelH = ttk.Label(mainframe, text=chr(letra))
    labelH.configure(anchor="center")
    labelH.grid(row=0, column=i+1, sticky="nsew")
    labelH['relief'] = 'raised'
    labelH.bind("<ButtonPress-1>", lambda e: changeColor())
    letra+=1

#LabelLeft
for j in range(4):
    labelV = ttk.Label(mainframe, text=j+1)
    labelV['width'] = 10
    labelV.configure(anchor="center")
    labelV['relief'] = 'raised'
    labelV.grid(row=j+1, column=0, sticky="nsew")

#Entrys
textoEntry = StringVar()
for i in range(4):
    for j in range(0,4):
        textoEntry.set(j)
        entrada = ttk.Entry(mainframe)
        entrada.grid(row=i+1, column=j+1, sticky="nsew")

root.mainloop()