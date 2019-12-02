import tkinter


def click(variable, value):
    variable.set(variable.get() + value)


def change(widget1, widget2, widget3):
    widget1.config(bg='blue')
    widget2.config(bg='red')
    widget3.config(bg='green')


if __name__ == '__main__':
    window = tkinter.Tk()

    frame = tkinter.Frame(window)
    frame.pack(side='left')

    frame2 = tkinter.Frame(window)
    frame2.pack(side='left')

    frame3 = tkinter.Frame(window)
    frame3.pack(side='left')

    frame4 = tkinter.Frame(window)
    frame4.pack(side='left')

    frame5 = tkinter.Frame(window)
    frame5.pack(side='right')

    counter = tkinter.IntVar()
    counter.set(255)

    counter2 = tkinter.IntVar()
    counter2.set(255)

    counter3 = tkinter.IntVar()
    counter3.set(255)

    labelRed = tkinter.Label(frame, text='Red', height=3)
    labelRed.pack()
    button1 = tkinter.Button(frame2, text="-", height=3, command=lambda: click(counter, -5))
    button1.pack()
    labelRedNum = tkinter.Label(frame3, text='255', anchor='center', bg='red', height=3, width=5, textvariable=counter)
    labelRedNum.pack()
    button2 = tkinter.Button(frame4, text="+", height=3, command=lambda: click(counter, +5))
    button2.pack()

    labelGreen = tkinter.Label(frame, text='Green', height=3)
    labelGreen.pack()
    button3 = tkinter.Button(frame2, text="-", height=3, command=lambda: click(counter2, -5))
    button3.pack()
    labelGreenNum = tkinter.Label(frame3, text='255', anchor='center', bg='green', height=3, width=5, textvariable=counter2)
    labelGreenNum.pack()
    button4 = tkinter.Button(frame4, text="+", height=3, command=lambda: click(counter2, +5))
    button4.pack()

    labelBlue = tkinter.Label(frame, text='Blue', height=3)
    labelBlue.pack()
    button5 = tkinter.Button(frame2, text="-", height=3, command=lambda: click(counter3, -5))
    button5.pack()
    labelBlueNum = tkinter.Label(frame3, text='255', anchor='center', bg='blue', height=3, width=5, textvariable=counter3)
    labelBlueNum.pack()
    button6 = tkinter.Button(frame4, text="+", height=3, command=lambda: click(counter3, +5))
    button6.pack()

    button7 = tkinter.Button(frame5, text="Mix", height=12, width=5, command=lambda: change(labelRedNum, labelBlueNum, labelGreenNum))
    button7.pack()

    window.mainloop()
