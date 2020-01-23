from tkinter import *
from tkinter import ttk


def newWindow(r:Tk):

    new=Toplevel(r)

    mainframe = ttk.Frame(new)
    mainframe.pack()
    mainframe['padding'] = 30

    lf = ttk.Labelframe(mainframe, text='THEMES')
    lf.pack()

    s = ttk.Style()
    var = StringVar()
    var.set(s.theme_use())
    for t in s.theme_names():
        ttk.Radiobutton(lf, text=t, variable=var, value=t, command=lambda: s.theme_use(var.get())).pack(anchor='w')

    s.theme_use('default')
    n = IntVar(0)
    Spinbox(lf, from_=0, to=100, textvariable=n).pack()
    ttk.Progressbar(lf, orient=HORIZONTAL, length=200, mode='determinate', variable=n).pack()

    new.update()
    new.minsize(new.winfo_width(), new.winfo_height())



