from tkinter import *
from tkinter import ttk


def mouseClick():
    print(labelColor.grid_info())

def setColor():
    color = comboValor.get()
    if color == 'Espanita':
        espanita()
    for i in range(0,4):
        if checkButtonsH[i].instate(['selected']):
            for j in range(0,4):
                if checkButtonsV[j].instate(['selected']):
                    if(j == 0):
                        labels[i]['background'] = color
                    if(j == 1):
                        labels[i+4]['background'] = color
                    if (j == 2):
                        labels[i + 8]['background'] = color
                    if (j == 3):
                        labels[i + 12]['background'] = color


def clearColor():
    for z in range(0, 16):
        labels[z]['background'] = ""
    # color = comboValor.get()
    # if color != 'Espanita':
    #     for z in range(0,16):
    #         labels[z]['background'] = ""


def espanita():
    for z in range(0,4):
        labels[z]['background'] = "red"
    for h in range(0,4):
        labels[h+4]['background'] = "yellow"
    for x in range(0,4):
        labels[x+8]['background'] = "red"


window = Tk()
window.title("GridColor")
window.minsize(420,280)
# window.maxsize(550,360)

frame = ttk.Frame(window)
frame.pack()


#Labels
labels = []
filaLabel = 0
columnaLabel = 1
labelStatus = StringVar()

for j in range(0,4):
    filaLabel+=1
    columnaLabel = 1
    for x in range(0, 4):
        labelColor = ttk.Label(frame, text="COLOR", textvariable=labelStatus)
        labelColor.grid(row=filaLabel, column=columnaLabel, sticky='nswe')
        labelColor['relief'] = 'sunken'
        labelColor.bind("<Button-1>", lambda e: mouseClick())
        labelColor['padding'] = (20, 20)
        labels.append(labelColor)
        columnaLabel+=1

#Checks
checkButtonsV = []
checkButtonsH = []

for z in range(0,4):
    check = ttk.Checkbutton(frame)
    check.grid(row=0, column=z+1, sticky='nswe')
    checkButtonsH.append(check)
for z in range(0, 4):
    check2 = ttk.Checkbutton(frame)
    check2.grid(row=z+1, column=0, sticky='nswe')
    checkButtonsV.append(check2)

#Buttons
buttonSet = ttk.Button(frame, text="SET", command=lambda: setColor())
buttonSet.grid(row=0, column=0)

buttonClear = ttk.Button(frame, text="CLEAR", command=lambda: clearColor())
buttonClear.grid(row=5, column=0)

#ComboBox
comboValor = StringVar()
comboColor = ttk.Combobox(frame, textvariable=comboValor)
comboColor.grid(row=5, column=1, columnspan=4, sticky='nswe')
comboColor['values'] = ('Red','Blue', 'Green', 'Espanita')


window.mainloop()
