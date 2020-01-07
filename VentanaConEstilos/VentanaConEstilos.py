from tkinter import *
from tkinter import ttk

root = Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

s = ttk.Style()
s.theme_use('clam')
s.configure('TLabel', font='STIXIntegralsUp')
s.theme_use('classic')
s.configure('TLabel', font='helvetica 14')

mainframe = ttk.Frame(root, relief='groove')
mainframe.grid(row=1, column=0)

styleframe = ttk.Frame(root, relief='groove')
styleframe.grid(row=2, column=0)

entryframe = ttk.Frame(root, relief='groove')
entryframe.grid(row=0, column=0)

note = ttk.Notebook(mainframe)
note.grid()

f1 = ttk.Frame(note)
f2 = ttk.Frame(note)
f3 = ttk.Frame(note)
note.add(f1, text='Ver')
note.add(f2, text='Editor')
note.add(f3, text='Colores')

labeltamanyo = ttk.Label(f1, text='Tamaño de letra')
labeltamanyo.grid(row=0, column=0)
tamanyo = Spinbox(f1, from_=0, to=100, width=5)
tamanyo.grid(row=0, column=1)

chbxnegrita = ttk.Checkbutton(f2, text='Negrita')
chbxnegrita.grid(row=1, column=0)
chbxcursiva = ttk.Checkbutton(f2, text='Cursiva')
chbxcursiva.grid(row=2, column=0)
chbxsub = ttk.Checkbutton(f2, text='Subrayado')
chbxsub.grid(row=3, column=0)

labelStyles = ttk.Label(styleframe, text='Selecciona un tema')
labelStyles.grid(row=0, column=0)

tema = StringVar()
combo = ttk.Combobox(styleframe, textvariable=tema)
combo['values'] = s.theme_names()
combo.bind('<<ComboboxSelected>>', lambda e: s.theme_use(tema.get()))
combo.grid()

buttonRestablecer = ttk.Button(styleframe, text='Restablecer')
buttonRestablecer.grid(row=3, column=0)

entrada = ttk.Entry(entryframe, width=40)
entrada.grid(row=0, column=0, sticky='nwse')

root.update()
root.minsize(root.winfo_width(), root.winfo_height())
root.mainloop()