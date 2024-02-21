from tkinter import *
from wordle import *

word1 = wordR()
print(word1)

ent = []
test1 = []

a = int(0)
go = int(0)
StopPoint = int(0)

gui = Tk()
gui.geometry('600x700')

# function get info from a key press
def kep_pressed(event):
    global a
    global go
    global StopPoint
    global test1

    if ( event.char == '\x08' ) and ( a > StopPoint ):
        a-=1
        ent[a]['text']=''
        if a%5 < 5:
            go = 0
    elif ( event.char == '\r' ):
        go = 0

        test1 = [ 
            ent[a-5]['text'],
            ent[a-4]['text'],
            ent[a-3]['text'],
            ent[a-2]['text'],
            ent[a-1]['text']
        ]
        test1 = "".join(test1)
        check(test1)
        #f = open("wordlist.txt","r", encoding="utf-8-sig")
        #if f"{test1}\n" in f.readlines():
            
        #f.close()      
    elif (not ( event.char == ' ' or len(event.keysym)>2 )) and ( go == 0 ):
        ent[a]['text']=event.char.lower()
        a+=1
        if a%5 == 0 and a != 0:
            go = 1

# Function Check chars with colors
def check(word2):
    count1 = 0
    global StopPoint
    StopPoint = a
    print(a)
    
    for x in word2:
        if x == word1[count1]:
            color = "green"
        elif x in word1:
            color = "yellow"
        else:
            color = "gray"
        
        ent[a-(5-count1)]['bg'] = color
        count1 +=1
    #if word1 == word2:
    #    exit()

# Frame for Wordle blocks
# @Jeagor and @Aleksasnder
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

gui.bind('<Key>', kep_pressed)
gui.mainloop()