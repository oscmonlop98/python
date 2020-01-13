from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox


def newWindow():
    new=Toplevel(root)
    var = StringVar()
    var.set('2')
    R1 = ttk.Radiobutton(new, text="Option 1", variable=var, value='1')
    R1.pack()
    R2 = ttk.Radiobutton(new, text="Option 2", variable=var, value='2')
    R2.pack()
    R3 = ttk.Radiobutton(new, text="Option 3", variable=var, value='3')
    R3.pack()
    new.grab_set()


def minimizar():
    if messagebox.askyesno(message='Angeles está loca?', icon = 'question', title = 'Install'):
        root.destroy()
    else:
        messagebox.showinfo(message='Como está loca ahí lo llevas')
        for i in range(0,100):
            new = Toplevel(root)
            label = ttk.Label(new, text="TENGO MUCHA ENERGÍA!!")
            label.pack()


root = Tk()
ttk.Button(root, text="New window", command=newWindow).pack()
ttk.Button(root, text="Minimize", command=minimizar).pack()


root.geometry('350x200')
root.mainloop()