from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from childw import newWindow


def minimizar():
    if messagebox.askyesno(message='Quieres cerrar?', icon = 'question', title = 'Install'):
        root.destroy()


root = Tk()
ttk.Button(root, text="New window", command=lambda: newWindow(root)).pack()
ttk.Button(root, text="Exit", command=minimizar).pack()

# **********ESTILOS*************
s = ttk.Style()
s.configure('TRadiobutton', font='Sans 12', padding=10)
s.theme_use('clam')
s.configure('TRadiobutton', font='Sans 12', padding=10)
s.theme_use('classic')
s.configure('TRadiobutton', font='Sans 12', padding=10)
s.theme_use('alt')
s.configure('TRadiobutton', font='Sans 12', padding=10)
s.theme_use('clam')

popmenu = Menu(root, tearoff=0)
for i in ('One', 'Two', 'Three'):
    popmenu.add_command(label=i)

root.bind('<3>', lambda e: popmenu.post(e.x_root, e.y_root))
root.bind('<1>', lambda e: popmenu.unpost())

root.geometry('350x200')
root.update()
root.minsize(root.winfo_width(), root.winfo_height())
root.mainloop()