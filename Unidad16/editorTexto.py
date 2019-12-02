import tkinter
from tkinter.font import Font


def cambiarFuente():
    if bold_checked.get():
        myFont = Font(weight="bold")
        entry.configure(font=myFont)
    else:
        myFont = Font()
        entry.configure(font=myFont)

    if cursiva_checked.get():
        myFont = Font(slant='italic')
        entry.configure(font=myFont)
    if underline_checked.get():
        myFont = Font(underline='true')
        entry.configure(font=myFont)


if __name__ == '__main__':
    window = tkinter.Tk()

    frame = tkinter.Frame(window)
    frame.pack()

    entry = tkinter.Entry(frame)
    entry.pack()

    bold_checked = tkinter.IntVar()
    cursiva_checked = tkinter.IntVar()
    underline_checked = tkinter.IntVar()

    checkBold = tkinter.Checkbutton(frame, text="Bold", variable=bold_checked)
    checkBold.pack(side="left")

    checkCursiva = tkinter.Checkbutton(frame, text="Cursiva", variable=cursiva_checked)
    checkCursiva.pack(side="left")

    checkUnderline = tkinter.Checkbutton(frame, text="Underline", variable=underline_checked)
    checkUnderline.pack(side="left")

    buttonUpdate = tkinter.Button(frame, text="Update", command=lambda: cambiarFuente())
    buttonUpdate.pack()

    window.mainloop()
