import tkinter


def get_text():
    content = body.get(1.0, "end-1c")
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    for i in content:
        if i == 'A' or i == 'a':
            count1 = count1 + 1
            countA.set(count1)
        if i == 'T' or i == 't':
            count2 = count2 + 1
            countT.set(count2)
        if i == 'C' or i == 'c':
            count3 = count3 + 1
            countC.set(count3)
        if i == 'G' or i == 'g':
            count4 = count4 + 1
            countG.set(count4)
    resul = "Num As:{} Num Ts:{} Num Cs:{} Num Gs:{}"
    resultado.set(resul.format(count1,count2,count3,count4))


def quit(root):
    root.destroy()


if __name__ == '__main__':
    window = tkinter.Tk()

    frame = tkinter.Frame(window)
    frame.pack()

    menubar = tkinter.Menu(window)
    filemenu = tkinter.Menu(menubar)
    filemenu.add_command(label='Quit', command=lambda: quit(window))

    menubar.add_cascade(label='File', menu=filemenu)
    window.config(menu=menubar)

    countA = tkinter.IntVar()
    countA.set(0)

    countT = tkinter.IntVar()
    countT.set(0)

    countC = tkinter.IntVar()
    countC.set(0)

    countG = tkinter.IntVar()
    countG.set(0)

    resultado = tkinter.StringVar()
    resultado.set("Num As: Num Ts: Num Cs: Gs:")

    body = tkinter.Text(frame, height=10, width=20)
    body.pack()

    button = tkinter.Button(frame, text="Contar letras", command=get_text)
    button.pack()

    labelCount = tkinter.Label(frame, textvariable=resultado)
    labelCount.pack()

    window.mainloop()

