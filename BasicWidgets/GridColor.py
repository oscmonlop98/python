from tkinter import *
from tkinter import ttk


def setColor():
    for i in range(0,6,2):
        for j in range(1,7,2):
            if checkButtons[i].instate(['selected']) and checkButtons[j].instate(['selected']):
                print(checkButtons[i].instate(['selected']) and checkButtons[j].instate(['selected']))
                # labels[i]['background'] = "red"
            # labels[1]['background'] = "blue"
            # labels[2]['background'] = "green"
            # labels[3]['background'] = "black"


#labelColor11['background'] = "red"
#if(comboColor.get()=='Red'):
# def clearColor():
#     labelColor11['background'] = ""


window = Tk()
window.title("GridColor")
window.minsize(420,280)
window.maxsize(550,360)

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
        labelColor.grid(row=filaLabel, column=columnaLabel)
        labelColor['relief'] = 'sunken'
        labelColor['padding'] = (20, 20)
        labels.append(labelColor)
        columnaLabel+=1

#Checks
checkButtons = []

for z in range(0,4):
    check = ttk.Checkbutton(frame)
    check.grid(row=0, column=z+1)
    check2 = ttk.Checkbutton(frame)
    check2.grid(row=z+1, column=0)
    checkButtons.append(check)
    checkButtons.append(check2)


#Buttons
buttonSet = ttk.Button(frame, text="SET", command=lambda: setColor())
buttonSet.grid(row=0, column=0)

buttonClear = ttk.Button(frame, text="CLEAR", command=lambda: clearColor())
buttonClear.grid(row=5, column=0)

#ComboBox
comboColor = ttk.Combobox(frame)
comboColor.grid(row=5, column=1, columnspan=4)
comboColor['values'] = ('Red','Blue', 'Green', 'Espanita')


# check01 = ttk.Checkbutton(frame)
# check01.grid(row=0, column=1)
#
# check02 = ttk.Checkbutton(frame)
# check02.grid(row=0, column=2)
#
# check03 = ttk.Checkbutton(frame)
# check03.grid(row=0, column=3)
#
# check04 = ttk.Checkbutton(frame)
# check04.grid(row=0, column=4)
#
# check10 = ttk.Checkbutton(frame)
# check10.grid(row=1, column=0)
#
# check20 = ttk.Checkbutton(frame)
# check20.grid(row=2, column=0)
#
# check30 = ttk.Checkbutton(frame)
# check30.grid(row=3, column=0)
#
# check40 = ttk.Checkbutton(frame)
# check40.grid(row=4, column=0)


#Labels
# labelColor11 = ttk.Label(frame, text="COLOR")
# labelColor11.grid(row=1, column=1)
# labelColor11['relief'] = 'sunken'
# labelColor11['padding'] = (20,20)
#
# labelColor12 = ttk.Label(frame, text="COLOR")
# labelColor12.grid(row=1, column=2)
# labelColor12['relief'] = 'sunken'
# labelColor12['padding'] = (20,20)
#
# labelColor13 = ttk.Label(frame, text="COLOR")
# labelColor13.grid(row=1, column=3)
# labelColor13['relief'] = 'sunken'
# labelColor13['padding'] = (20,20)
#
# labelColor14 = ttk.Label(frame, text="COLOR")
# labelColor14.grid(row=1, column=4)
# labelColor14['relief'] = 'sunken'
# labelColor14['padding'] = (20,20)
#
# labelColor21 = ttk.Label(frame, text="COLOR")
# labelColor21.grid(row=2, column=1)
# labelColor21['relief'] = 'sunken'
# labelColor21['padding'] = (20,20)
#
# labelColor22 = ttk.Label(frame, text="COLOR")
# labelColor22.grid(row=2, column=2)
# labelColor22['relief'] = 'sunken'
# labelColor22['padding'] = (20,20)
#
# labelColor23 = ttk.Label(frame, text="COLOR")
# labelColor23.grid(row=2, column=3)
# labelColor23['relief'] = 'sunken'
# labelColor23['padding'] = (20,20)
#
# labelColor24 = ttk.Label(frame, text="COLOR")
# labelColor24.grid(row=2, column=4)
# labelColor24['relief'] = 'sunken'
# labelColor24['padding'] = (20,20)
#
# labelColor31 = ttk.Label(frame, text="COLOR")
# labelColor31.grid(row=3, column=1)
# labelColor31['relief'] = 'sunken'
# labelColor31['padding'] = (20,20)
#
# labelColor32 = ttk.Label(frame, text="COLOR")
# labelColor32.grid(row=3, column=2)
# labelColor32['relief'] = 'sunken'
# labelColor32['padding'] = (20,20)
#
# labelColor33 = ttk.Label(frame, text="COLOR")
# labelColor33.grid(row=3, column=3)
# labelColor33['relief'] = 'sunken'
# labelColor33['padding'] = (20,20)
#
# labelColor34 = ttk.Label(frame, text="COLOR")
# labelColor34.grid(row=3, column=4)
# labelColor34['relief'] = 'sunken'
# labelColor34['padding'] = (20,20)
#
# labelColor41 = ttk.Label(frame, text="COLOR")
# labelColor41.grid(row=4, column=1)
# labelColor41['relief'] = 'sunken'
# labelColor41['padding'] = (20,20)
#
# labelColor42 = ttk.Label(frame, text="COLOR")
# labelColor42.grid(row=4, column=2)
# labelColor42['relief'] = 'sunken'
# labelColor42['padding'] = (20,20)
#
# labelColor43 = ttk.Label(frame, text="COLOR")
# labelColor43.grid(row=4, column=3)
# labelColor43['relief'] = 'sunken'
# labelColor43['padding'] = (20,20)
#
# labelColor44 = ttk.Label(frame, text="COLOR")
# labelColor44.grid(row=4, column=4)
# labelColor44['relief'] = 'sunken'
# labelColor44['padding'] = (20,20)

window.mainloop()
