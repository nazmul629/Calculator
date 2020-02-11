from tkinter import *
 
root = Tk()
root.geometry("400x550+200+100")
root.title("Calculator")
root.configure(background='black')
root.resizable(False,False)



# ............EnttryBox...........
entry_box = Entry(font="arial 20 bold",bg = "powder blue",bd = 6,width=22, justify = RIGHT)
entry_box.insert(0,"0")
entry_box.place(x=30,y=10)

#  Enty data in  Entry 
def ente_number(x):
    if entry_box.get() =="0":
        if x == '.':
            entry_box.insert(1,'.')
        else:
            entry_box.delete(0,'end')
            entry_box.insert(0,str(x))
    else:
        length = len(entry_box.get())
        entry_box.insert(length,str(x))


def enter_oprator(x):
    if entry_box.get() !="0":
        length = len(entry_box.get())

        all_text = entry_box.get()
        last_char = all_text[-1:]
        if last_char in ['+','-','*','/'] or all_text[-2:] == '**':
            pass 
        else:
            entry_box.insert(length,btn_oprator[x]['text'])



def clear_fun():
    entry_box.delete(0,END)
    entry_box.insert(0,'0')

result = 0
history=[]
def equal_fun():
    content = entry_box.get()
    result = eval(content) # Opration  
    entry_box.delete(0,END)  # delete Last element 
    entry_box.insert(0,result) # if last element equeal null then insurt 0
    
    history.append(content)
    history.reverse()
    status.configure(text="History:"+' | '.join(history[:4]),font = "arial 15 bold")

def del_fun():
    length = len(entry_box.get())
    entry_box.delete(length-1,'end')
    if length == 1:
        entry_box.insert(0,'0')
    
# ........... 1-9 Button.............
button_numbers = []
for i in range(10):
    button_numbers.append(Button(font="arial 15 bold",width=4,bd=6, text=str(i),command = lambda x=i:ente_number(x)))

btn_text = 1
for row in range(0,3):
    for col in range(0,3):
        button_numbers[btn_text].place(x=30+col*90,y=70+row*70)
        btn_text+=1


# ------------0 button-----------
btn_zero = Button(width=4,text='0',bd=6,font="arial 15 bold",command = lambda x = 0 :ente_number(x))
btn_zero.place(x = 25,y= 280)

# ...........Dot Button..............
btn_dot = Button(width=4,text='.',bd=6,font="arial 15 bold",command = lambda x =  '.':ente_number(x))
btn_dot.place(x = 115,y= 280)

# ...........Equeal Button..............
btn_equal = Button(width=4,text='=',bd=6,font="arial 15 bold",command = equal_fun)
btn_equal.place(x = 205,y=280)

#........... Clear C Button.............
btn_clear = Button(width=6,text="C",font="arial 15 bold", bd=6,command=clear_fun)
btn_clear.place(x=25,y=340)

#........... Clear C Button.............
btn_del= Button(width=6,text="del",font="arial 15 bold", bd=6,command=del_fun)
btn_del.place(x=280,y=340)

# ------------Status-------
status = Label(root,text="History:", relief=SUNKEN, font="arial 15 bold",anchor = W,height= 2)
status.pack(side=BOTTOM,fill=X)


# ------- oprator button----------
btn_oprator = []
for i in range(4):
    btn_oprator.append(Button(font="arial 14 bold",width=4,bd=6, text=str(i),command=lambda x = i:enter_oprator(x)))

btn_oprator[0]['text'] = '+'
btn_oprator[1]['text'] = '-'
btn_oprator[2]['text'] = '*'
btn_oprator[3]['text'] = '/'

for i in range(4):
    btn_oprator[i].place(x=300,y=70+i*70)





root.mainloop()
