from tkinter import *
from tkinter import ttk
from tkinter import font

root = Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

s = ttk.Style()
s.theme_use('clam')
s.configure('TLabel', font='STIXIntegralsUp')
s.theme_use('classic')
s.configure('TLabel', font='helvetica 60')

mainframe = ttk.Frame(root)
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
mainframe.grid()

label = ttk.Label(mainframe, text="Label", style='TLabel')
label['padding'] = (20,20)
label['relief'] = 'raised'
label.grid(row=0, column=0, pady=10)

button = ttk.Button(mainframe, text="Click me")
button.grid(row=1, column=0, pady=10)

check = ttk.Checkbutton(mainframe, text="Check")
check.grid(row=2, column=0, pady=30)

tema = StringVar()
combo = ttk.Combobox(mainframe, textvariable=tema)
combo['values'] = s.theme_names()
combo.bind('<<ComboboxSelected>>', lambda e: s.theme_use(tema.get()))
combo.grid()
print(font.families())
root.update()
root.minsize(root.winfo_width(), root.winfo_height())
root.mainloop()
