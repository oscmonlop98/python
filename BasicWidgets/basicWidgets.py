from tkinter import *
from tkinter import ttk


def refreshStates():
    buttonStatus.set(button.state())
    labelStatus.set(label2.state())
    checkStatus.set(checkbutton.state())
    radioStatus1.set(radio1.state())
    radioStatus2.set(radio2.state())
    radioStatus3.set(radio3.state())
    comboStatus.set(combo.state())

def cambiarEstado():
    checkbutton['state'] = 'active'
    # if button.instate(['disabled']):
    #     button['state'] = 'normal'
    # else:
    #     button['state'] = 'disabled'
    # if checkInfo.get() == 0 and checkbutton.instate(['hover']):
    #     checkInfo.set(1)
    #     checkbutton['state'] = 'active'
    # else:
    #     checkInfo.set(0)



window = Tk()
window.title("Hola")

frame = ttk.Frame(window)
frame['padding'] = (30,30,30,30)
frame['borderwidth'] = 10
frame['relief'] = 'ridge'
frame.pack()

#Label
labelStatus = StringVar()
label3 = ttk.Label(frame, textvariable=labelStatus)
label3.grid(row=9, column=0)

label2 = ttk.Label(frame)
label2['relief'] = GROOVE
label2['text'] = "ssdasdas"
label2.grid(row=8, column=0)

#Button
buttonStatus = StringVar()

label = ttk.Label(frame, textvariable=buttonStatus)
label.grid(row=0, column=1)

button = ttk.Button(frame, text="Press")
button['state'] = 'disabled'
button.grid(row=0, column=0)

#CheckButton
checkStatus = StringVar()
checkInfo = IntVar()

labelCheck = ttk.Label(frame, textvariable=checkStatus)
labelCheck.grid(row=1, column=1)

checkbutton = ttk.Checkbutton(frame, text='Check', variable=checkInfo)
checkbutton.grid(row=1, column=0)

#RadioButton
radioStatus1 = StringVar()
radioStatus2 = StringVar()
radioStatus3 = StringVar()
radios = StringVar()

labelRadio1 = ttk.Label(frame, textvariable=radioStatus1)
labelRadio1.grid(row=2, column=1)

labelRadio2 = ttk.Label(frame, textvariable=radioStatus2)
labelRadio2.grid(row=3, column=1)

labelRadio3 = ttk.Label(frame, textvariable=radioStatus3)
labelRadio3.grid(row=4, column=1)

radio1 = ttk.Radiobutton(frame, text='Uno', variable=radios, value='uno')
radio2 = ttk.Radiobutton(frame, text='Dos', variable=radios, value='dos')
radio3 = ttk.Radiobutton(frame, text='Tres', variable=radios, value='tres')
radio1.grid(row=2, column=0)
radio2.grid(row=3, column=0)
radio3.grid(row=4, column=0)

#ComboBox
comboStatus = StringVar()

labelCombo = ttk.Label(frame, textvariable=comboStatus)
labelCombo.grid(row=5, column=1)
combo = ttk.Combobox(frame, text='Combo')
combo.grid(row=5, column=0)
combo['values'] = ('USA','ESPAÑA', 'CATALONIA INDEPENDENT')
combo.state(['readonly'])

#Button
buttonCambio = ttk.Button(frame, text='Cambiar Estado', command=lambda: cambiarEstado())
buttonCambio.grid(row=6, column=0)

window.bind("<Return>", lambda e: refreshStates())


window.mainloop()