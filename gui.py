from tkinter import *
from wordle import *

ent = []

gui = Tk()
gui.geometry('600x700')


LabStatus1 = Label(gui,text = wordR(),bg="white",font="Arial 24",width=14, borderwidth=4, relief="solid")

# status for a word
# @Jegor 
text_frame = Frame(gui)
text_frame.pack(pady=0)
LabStatus = Label(text_frame,text = ' ',bg="white",font="Arial 24",width=14, borderwidth=4, relief="solid")
LabStatus.grid(row=0,column=0)

# Frame for Wordle blocks
# @Jegor and @Aleksasnder
wordle_frame = Frame(gui)
wordle_frame.pack(pady=0)
for i in range(30):
    ent.append(Label(wordle_frame,text = ' ',bg="white",font="Arial 24",width=2, borderwidth=4, relief="solid"))
    #ent[i].place(height=40, width=40)
    #ent[i].place(x = (50 * ( i % 5 )), y = (50 * (i // 5) ))
    ent[i].grid( row=( i // 5 ), column=( i%5 ), padx=5, pady=5)

# Frame for key in a keyboard
# @Jeagor
alphabet_frame = Frame(gui)
alphabet_frame.pack(pady=10)
alphabet_rows = ["абвгдеёжзийклм", "нопрстуфхцчшщъ", "ыьэюя"]
alphabet_buttons = {}
for row in alphabet_rows:
    row_frame = Frame(alphabet_frame)
    row_frame.pack()
    for letter in row:
        button = Button(row_frame, text=letter, font=("Arial", 14), width=1, height=1, bg='white')
        button.pack(side=LEFT, padx=5)
        alphabet_buttons[letter] = button


button_frame = Frame(gui)
button_frame.pack(pady=0)
BTN = Button(button_frame,text = 'menu',bg="white",font="Arial 24",width=4, borderwidth=4, relief="solid",command=lambda ent=ent, LabStatus1=LabStatus1,LabStatus=LabStatus: [WinWordleWindow(LabStatus1,ent,LabStatus) ])
BTN.grid(row=0,column=0)

#WinWordleWindow

gui.bind('<Key>',lambda event, ent=ent, LabStatus1=LabStatus1,LabStatus=LabStatus:kep_pressed(event, LabStatus1, ent, LabStatus)) 
gui.mainloop()