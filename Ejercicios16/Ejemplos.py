import tkinter

# The controller.
def click(variable, value):
    variable.set(variable.get() + value)


if __name__ == '__main__':
    window = tkinter.Tk()

# The model.
    counter = tkinter.IntVar()
    counter.set(0)

    # The views.
    frame = tkinter.Frame(window)
    frame.pack()

    button = tkinter.Button(frame, text='Up', command=lambda: click(counter, +1))
    button.pack()

    button = tkinter.Button(frame, text='Down', command=lambda: click(counter, -1))
    button.pack()

    label = tkinter.Label(frame, textvariable=counter)
    label.pack()

    # Start the machinery!
    window.mainloop()
