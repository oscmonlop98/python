from tkinter import *
from tkinter import ttk

window = Tk()

mainframe = Frame(window)
mainframe.grid()

#Entry
textoEntry = StringVar()
for i in range(4):
    for j in range(0,4):
        textoEntry.set(j)
        entrada = Entry(mainframe, textvariable=textoEntry)
        entrada.grid(row=i, column=j)

window.mainloop()