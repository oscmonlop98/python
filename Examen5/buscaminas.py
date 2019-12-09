from tkinter import *
from tkinter import ttk
from random import randint


def putMine(prob):
   if randint(1, prob) == 1:
       return 1
   else:
       return 0


def comprobar(widget, listaminas):
        lbl_array[r][c].set('0')


def mouseClick(a):
    print(a.get())
    if a.get() == 1:
        stReady.set("You Looser")
        lblReady['background'] = 'red'


root = Tk()
root.title("Buscaminas Oscar Moreno")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

mainframe = ttk.Frame(root,relief='raised')

for i in range(0,11):
    mainframe.columnconfigure(i, weight=1, minsize='20p')
    mainframe.rowconfigure(i, weight=1, minsize='20p')
mainframe.grid(column=0, row=0)
mainframe['padding'] = (2,2,22,22)


#Labels parrilla
lblgrid = list()
str_array = list()
mine_array = list()
for r in range(10):
    lblgrid.append([])
    str_array.append([])
    for c in range(10):
        str_array[r].append(StringVar())
        lblgrid[r].append(ttk.Label(mainframe, relief='groove', textvariable=str_array[r][c]))
        lblgrid[r][c].grid(row=r+1, column=c+1, sticky='nwse')
        #Aquí meto las minas
        mine_array.
        mine_array.append(lbl_array[r][c])
        lbl_array[r][c].set('')
lblgrid[r][c].bind("<Enter>", lambda e: comprobar(lbl_array[r][c], mine_array))
lblgrid[r][c].bind("<Button-1>", lambda e: mouseClick(lbl_array[r][c]))

#Label inferior
stReady = StringVar()
stReady.set("Ready to play!")
lblReady = ttk.Label(mainframe, relief='groove', textvariable=stReady)
# lblReady['text'] = "Ready to play!"
lblReady.configure(anchor="center")
lblReady.grid(row=11, column=1, columnspan=5, sticky='nwse')

#Button
btNewGame = ttk.Button(mainframe)
btNewGame['text'] = "New game!"
btNewGame.grid(row=11, column=6, columnspan=5, sticky='nwse')

root.update()
root.minsize(root.winfo_width(), root.winfo_height())
root.mainloop()