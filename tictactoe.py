from tkinter import *

root=Tk()
buttons = ['b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9']
rw=1
clmn=1
count=1
for name in buttons:
    
    name=Button(root, text='', width=6, height=3, bg='silver', command=lambda :clicked(name))
    name.grid(column=clmn, row=rw)
    
    if clmn==3:
        clmn=1
    else:
        clmn+=1
    if count==3 or count==6:
        rw+=1
    count+=1

def clicked(l):
        if l['text']=='':
            l.config(text='X')
            #print(type(l))

mainloop()