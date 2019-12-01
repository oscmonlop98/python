from tkinter import *
root = Tk()
aa = 'Question #'
labels=[] #creates an empty list for your labels
fila = 0
columna = 1

for j in range(0,4):
    fila+=1
    columna = 1
    for x in range(0, 4): #iterates over your nums
        label = Label(root, text="COLOR")
        label.grid(row=fila, column=columna)
        label['relief'] = 'sunken'
        labels.append(label)
        columna+=1

root.mainloop()
