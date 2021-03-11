from tkinter import *
from tkinter import messagebox
root=Tk()

b1=Button(root, text='', width=6, height=3, bg='silver', command=lambda :clicked(b1))
b2=Button(root, text='', width=6, height=3, bg='silver', command=lambda :clicked(b2))
b3=Button(root, text='', width=6, height=3, bg='silver', command=lambda :clicked(b3))
b4=Button(root, text='', width=6, height=3, bg='silver', command=lambda :clicked(b4))
b5=Button(root, text='', width=6, height=3, bg='silver', command=lambda :clicked(b5))
b6=Button(root, text='', width=6, height=3, bg='silver', command=lambda :clicked(b6))
b7=Button(root, text='', width=6, height=3, bg='silver', command=lambda :clicked(b7))
b8=Button(root, text='', width=6, height=3, bg='silver', command=lambda :clicked(b8))
b9=Button(root, text='', width=6, height=3, bg='silver', command=lambda :clicked(b9))

buttons = [[b1, b2, b3], [b4, b5, b6], [b7, b8, b9]]
rw=0
clmn=0
for i in buttons:
    for j in i:
        if clmn==3:
            clmn=0
        j.grid(column=clmn, row=rw)
        clmn=clmn+1
    rw=rw+1
cross=False
def clicked(l):
    global cross
    if l['text']==''and cross is False:
        l.config(text='O')
        cross=True 
    elif l['text']=='' and cross is True:
        l.config(text='X')
        cross=False
    checkifwon()

def checkifwon():
    #check in rows
    for w in buttons:
      s=w[0]
      d=w[1]
      f=w[2]
      if s['text']==d['text'] and s['text']==f['text']:
        if s['text']=='':
            pass
        else:
            wonr=[s, d, f]
            for i in wonr:
                i.config(bg='red')
            winner(s)
    #check in columns        
    for ind in range(3):
        e=buttons[0][ind]
        r=buttons[1][ind]
        t=buttons[2][ind]
        if e['text']==r['text'] and e['text']==t['text']:
            if e['text']=='':
                pass
            else:
                wonc=[e, r, t,]
                for i in wonc:
                    i.config(bg='red')
                winner(e)
    #check diagonally
    if b5['text']==b1['text'] and b5['text']==b9['text'] or b5['text']==b3['text'] and b5['text']==b7['text']:
        if b5['text']=='':
            pass
        else:
            if b5['text']==b1['text'] and b5['text']==b9['text']:
                b1.config(bg='red')
                b5.config(bg='red')
                b9.config(bg='red')
            elif b5['text']==b3['text'] and b5['text']==b7['text']:
                b3.config(bg='red')
                b5.config(bg='red')
                b7.config(bg='red')
            winner(b5)
def winner(h):
    messagebox.showinfo('Tic Tac Toe', h['text']+' WINS!')
    for i in buttons:
        for k in i:
            k.config(state=DISABLED)
mainloop()