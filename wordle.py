from random import *
from tkinter import *

a = int(0)
go = int(0)
StopPoint = int(0)

# get a random word
def wordR():
    f = open("wordlist.txt","r", encoding="utf-8-sig")
    MaxF = int(len(f.read())/6)
    f.close()

    f = open("wordlist.txt","r", encoding="utf-8-sig")
    Ra=randint(0,MaxF)
    word = (f.readlines())[Ra][:-1]
    f.close()
    print(word)
    return word

# Window Menu for new game and quits
def WinWordleWindow(LabStatus1,ent,LabStatus):
    gui = Tk()
    gui.geometry('400x100')
    button_frame = Frame(gui)
    button_frame.pack(pady=0)
    BTN_Exit = Button(button_frame,text = 'Exit',bg="white",font="Arial 24",width=6, borderwidth=4, relief="solid",command=exit)
    BTN_NewGame = Button(button_frame,text = 'New Game',bg="white",font="Arial 24",width=8, borderwidth=4, relief="solid",command=lambda ent=ent,LabStatus1=LabStatus1 ,LabStatus=LabStatus: ClearWordle(LabStatus1,ent,LabStatus) )
    BTN_Exit.grid(row=0,column=0)
    BTN_NewGame.grid(row=0,column=1)
    gui.mainloop()

# reset Wordle
def ClearWordle(LabStatus1,ent,LabStatus):
    global a
    global go
    global StopPoint
    a = 0
    go = 0
    StopPoint = 0
    for i in range(30):
        ent[i]['bg'] = "white"
        ent[i]['text'] = ""
    LabStatus1['text'] = wordR()
    LabStatus['text'] = ""
    
# function get info from a key press
def kep_pressed(event,LabStatus1,ent,LabStatus,alphabet_rows,alphabet_buttons):
    global a
    global go
    global StopPoint
    test1 = []
    #print(LabStatus1['text'])
    #print(a)

    if ( event.char == '\x08' ) and ( a > StopPoint ):
        a-=1
        ent[a]['text']=''
        if a%5 < 5:
            go = 0
    elif ( event.char == '\r' ) and (go == 1):
        go = 0
        test1 = [ 
            ent[a-5]['text'],
            ent[a-4]['text'],
            ent[a-3]['text'],
            ent[a-2]['text'],
            ent[a-1]['text']
        ]
        test1 = "".join(test1)
        f = open("wordlist.txt","r", encoding="utf-8-sig")
        if f"{test1}\n" in f.readlines():
            check(test1,LabStatus1,ent,LabStatus,alphabet_rows,alphabet_buttons)
        else:
            LabStatus['text']='word is not real' 
            go = 1
        f.close()      
    elif (not ( event.char == ' ' or len(event.keysym)>2 )) and ( go == 0 ):
        ent[a]['text']=event.char.lower()
        a+=1
        if a%5 == 0 and a != 0:
            go = 1
    
# Function Check chars with colors
def check(word2,LabStatus1,ent,LabStatus,alphabet_rows,alphabet_buttons):
    global a
    global StopPoint
    StopPoint = a
    count1 = 0
    LabStatus['text']=''
    for x in word2:
        for row in alphabet_rows:
            for letter in row:

                if ( x == letter  ):

                    if x == (LabStatus1['text'])[count1]:
                        color = "green"
                    elif x in str(LabStatus1['text']):
                        color = "yellow"
                    else:
                        color = "gray"

                    (alphabet_buttons[letter])["bg"] = color
                    ent[a-(5-count1)]['bg'] = color
                    count1 +=1
    if LabStatus1['text'] == word2:
        LabStatus['text']='Win'
        WinWordleWindow(LabStatus1,ent,LabStatus)
    elif a == 30:
        LabStatus['text']='lose' 
        WinWordleWindow(LabStatus1,ent,LabStatus)
