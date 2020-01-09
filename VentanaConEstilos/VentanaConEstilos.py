from tkinter import *
from tkinter import ttk


def donothing():
    t = Toplevel(root)
    mainframe = ttk.Frame(t)
    mainframe.grid(row=1, column=0)

    styleframe = ttk.Frame(t)
    styleframe.grid(row=2, column=0)

    note = ttk.Notebook(mainframe)
    note.grid()

    f1 = ttk.Frame(note)
    f2 = ttk.Frame(note)
    f3 = ttk.Frame(note)
    f4 = ttk.Frame(note)
    note.add(f1, text='Ver')
    note.add(f2, text='Editor')
    note.add(f3, text='Colores')
    note.add(f4, text='Complementos')

    # Ver
    cbnumerolinea = ttk.Checkbutton(f1, text='Mostrar los números de línea')
    cbnumerolinea.grid(row=0, column=0, sticky='w')

    cbmargen = ttk.Checkbutton(f1, text='Mostrar margen derecho en la columna: ')
    cbmargen.grid(row=1, column=0)
    tamanyo = Spinbox(f1, from_=0, to=100, width=5)
    tamanyo.grid(row=1, column=1, sticky='e')

    cbestado = ttk.Checkbutton(f1, text='Mostrar barra de estado')
    cbestado.grid(row=2, column=0, sticky='w')

    ajuste = ttk.Label(f1, text='Ajuste del texto')
    ajuste.grid(row=3, column=0, sticky='w')

    cbajuste = ttk.Checkbutton(f1, text='Activar ajuste de texto')
    cbajuste.grid(row=4, column=0, sticky='w')

    cbdividir = ttk.Checkbutton(f1, text='No dividir palabras sobre dos líneas')
    cbdividir.grid(row=5, column=0, sticky='w')

    resalte = ttk.Label(f1, text='Resalte')
    resalte.grid(row=6, column=0, sticky='w')

    cbresaltalinea = ttk.Checkbutton(f1, text='Resaltar la línea actual')
    cbresaltalinea.grid(row=7, column=0, sticky='w')

    cbresaltapareja = ttk.Checkbutton(f1, text='Resaltar parejas de corchetes')
    cbresaltapareja.grid(row=8, column=0, sticky='w')

    # Editar
    chbxnegrita = ttk.Checkbutton(f2, text='Negrita')
    chbxnegrita.grid(row=1, column=0, sticky='w')
    chbxcursiva = ttk.Checkbutton(f2, text='Cursiva')
    chbxcursiva.grid(row=2, column=0, sticky='w')
    chbxsub = ttk.Checkbutton(f2, text='Subrayado')
    chbxsub.grid(row=3, column=0, sticky='w')

    labelStyles = ttk.Label(styleframe, text='Selecciona un tema')
    labelStyles.grid(row=0, column=0)

    tema = StringVar()
    combo = ttk.Combobox(styleframe, textvariable=tema)
    combo['values'] = s.theme_names()
    combo.bind('<<ComboboxSelected>>', lambda e: s.theme_use(tema.get()))
    combo.grid(row=1, column=0)


def nuevahoja():
    hoja = ttk.Frame(hojastexto)

    hojastexto.add(hoja, text='New File')

    cajatexto = Text(hoja)
    cajatexto.grid(row=0, column=0, sticky='nwse')


root = Tk()
root.columnconfigure(0, weight=2)
root.rowconfigure(0, weight=2)

# **********MENÚ*************
menubar = Menu(root)
hojamenu = Menu(menubar, tearoff=0)
hojamenu.add_command(label="Hoja", command=nuevahoja)
menubar.add_cascade(label="Nueva", menu=hojamenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Preferencias", command=donothing)
menubar.add_cascade(label="Editar", menu=editmenu)

# **********ESTILOS*************
s = ttk.Style()
s.configure('TLabel', font='STIXIntegralsUp')
s.configure('TLabel', font=('Sans','15','bold'), padding=10)
s.configure('TCheckbutton', font='Sans 12', padding=10)
s.theme_use('clam')
s.configure('TLabel', font='STIXIntegralsUp')
s.configure('TLabel', font=('Sans','15','bold'), padding=10)
s.configure('TCheckbutton', font='Sans 12', padding=10)
s.theme_use('classic')
s.configure('TLabel', font='STIXIntegralsUp')
s.configure('TLabel', font=('Sans','15','bold'), padding=10)
s.configure('TCheckbutton', font='Sans 12', padding=10)
s.theme_use('alt')
s.configure('TLabel', font='STIXIntegralsUp')
s.configure('TLabel', font=('Sans','15','bold'), padding=10)
s.configure('TCheckbutton', font='Sans 12', padding=10)
s.theme_use('clam')

# **********FRAME*************
framehojas = ttk.Frame(root)
framehojas.columnconfigure(0, weight=1)
framehojas.rowconfigure(0, weight=1)
framehojas.grid(row=0, column=0, sticky='nwse')

# **********NOTEBOOK*************
hojastexto = ttk.Notebook(framehojas)
hojastexto.grid(sticky='nwse')

hoja1 = ttk.Frame(hojastexto)
hoja1.grid(sticky='nwse')

hojastexto.add(hoja1, text='New File')

cajatexto = Text(hoja1)
cajatexto.grid(row=0, column=0)


root.config(menu=menubar)
root.update()
root.minsize(root.winfo_width(), root.winfo_height())
root.mainloop()