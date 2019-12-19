from tkinter import *
from tkinter import ttk
from tkinter import colorchooser


def changeColor(widget):
    color = colorchooser.askcolor()
    widget['background'] = color[1]


root = Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

mainframe = ttk.Frame(root, relief='raised')
mainframe['padding'] = (20,20,20,20)
mainframe.grid()

labelColor = ttk.Label(mainframe, relief='raised')
labelColor['padding'] = (50,50)
labelColor.grid(row=0, column=0, sticky='nwse')

buttonColor = ttk.Button(mainframe, text="Change Color", command=lambda: changeColor(labelColor))
buttonColor['padding'] = (10)
buttonColor.grid(row=1, column=0)

root.update()
root.minsize(root.winfo_width(), root.winfo_height())
root.mainloop()