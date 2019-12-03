from tkinter import *
from tkinter import ttk

def termina():
    label1['background'] = 'red'
    print(label1.grid_info().get('column'))
    print(label2.grid_info().get('column'))

def dimeColumna(widget):
    x,y = widget.winfo_pointerxy()
    target = widget.winfo_containing(x,y)
    try:
        target['text'] = widget['text']
    except:
        pass

window = Tk()
window.minsize(420,280)

frame = ttk.Frame(window)
frame.pack()

label1 = ttk.Label(frame, text="1")
label1['padding'] = (20, 20)
label1['relief'] = 'sunken'
label1.grid(row=0, column=0)

label2 = ttk.Label(frame, text="2")
label2['padding'] = (20, 20)
label2['relief'] = 'sunken'
label2.grid(row=0, column=1)

label3 = ttk.Label(frame, text="3")
label3['padding'] = (20, 20)
label3['relief'] = 'sunken'
label3.grid(row=1, column=0)

label4 = ttk.Label(frame, text="4")
label4['padding'] = (20, 20)
label4['relief'] = 'sunken'
label4.grid(row=1, column=1)


label1.bind("<ButtonPress-1>")
# label1.bind("<B1-Motion>",lambda e: dimeColumna(label1))
label2.bind("<B1-Motion>",lambda e: dimeColumna(label2))
# label1.bind("<ButtonRelease-1>", lambda e: dimeColumna(label1))

window.mainloop()