from tkinter import *
from tkinter import ttk

class MoveManager():
    def add_dragable(self, widget):
        widget.bind("<Left>", self.on_start)
        widget.bind("<Right>", self.on_drag)
        widget.bind("<Up>", self.on_drop)
        widget.bind("<Down>", self.on_drop)

    def on_start(self, event):
        # you could use this method to create a floating window
        # that represents what is being dragged.
        pass

    def on_drag(self, event):
        # you could use this method to move a floating window that
        # represents what you're dragging
        pass

    def on_drop(self, event):
        # find the widget under the cursor
        x,y = event.widget.winfo_pointerxy()
        target = event.widget.winfo_containing(x,y)
        try:
            target['background'] = event.widget['background']
            event.widget['background'] = ''
        except:
            pass


def mover(widget):
    widget['background'] = 'red'


root = Tk()
root.title("Buscaminas Oscar Moreno")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

mainframe = ttk.Frame(root,relief='raised')

for i in range(0,21):
    mainframe.columnconfigure(i, weight=1, minsize='30p')
    mainframe.rowconfigure(i, weight=1, minsize='30p')
mainframe.grid(column=0, row=0)
mainframe['padding'] = (2,2,22,22)

#Labels parrilla
lblgrid = list()
lbl_array = list()
for r in range(20):
    lblgrid.append([])
    lbl_array.append([])
    for c in range(10):
        lbl_array[r].append(StringVar())
        lblgrid[r].append(ttk.Label(mainframe, relief='groove', textvariable=lbl_array[r][c]))
        root.bind('<Left>', lambda e: mover(lblgrid[r][c]))
        lblgrid[r][c].grid(row=r+1, column=c+1, sticky='nwse')
        #Aquí meto las minas
        lbl_array[r][c].set('')



#Label inferior
stReady = StringVar()
stReady.set("Ready to play!")
lblReady = ttk.Label(mainframe, relief='groove', textvariable=stReady)
# lblReady['text'] = "Ready to play!"
lblReady.configure(anchor="center")
lblReady.grid(row=21, column=1, columnspan=5, sticky='nwse')

#Button
btNewGame = ttk.Button(mainframe, command=lambda: mover(lblgrid[0][3]))
btNewGame['text'] = "New game!"
btNewGame.grid(row=21, column=6, columnspan=5, sticky='nwse')

root.update()
root.minsize(root.winfo_width(), root.winfo_height())
root.mainloop()