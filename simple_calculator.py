from tkinter import *
root = Tk()
root.title('Simple calculator')

e= Entry(root, width = 35, borderwidth = 5)
e.grid(column=0, row=0, columnspan=3, padx = 10, pady = 10)

#define button functions

def enter_value(number):
    e.insert(END, number)
    

def add():
    number1 = e.get()
    global num1 
    global math
    math = 'addition'
    num1 = float(number1)
    e.delete(0,END)

def equals():
    number2 = e.get()
    e.delete(0,END)
    if math == 'addition':
        e.insert(0,float(num1) + float(number2))
    elif math == 'subtraction':
        e.insert(0,float(num1) - float(number2))
    elif math == 'multiplication':
        e.insert(0,float(num1) * float(number2))
    elif math == 'division':
        e.insert(0,float(num1) / float(number2))

  

def clear():
    e.delete(0,END)

def subtract(minus):
    number1 = e.get()
    if number1 == '':
        e.insert(0,minus)
    else:
        global math
        math = 'subtraction'
        global num1 
        num1 = float(number1)
        e.delete(0,END)

def multiply():
    number1 = e.get()
    global math
    math = 'multiplication'
    global num1 
    num1 = float(number1)
    e.delete(0,END)

def divide():
    number1 = e.get()
    global math
    math = 'division'
    global num1 
    num1 = float(number1)
    e.delete(0,END)

    
#define buttons    
abutton1 = Button(root, text='1', padx=40, pady=20, command= lambda: enter_value(1))
abutton2 = Button(root, text='2', padx=40, pady=20, command= lambda: enter_value(2))
abutton3 = Button(root, text='3', padx=40, pady=20, command= lambda: enter_value(3))
abutton4 = Button(root, text='4', padx=40, pady=20, command= lambda: enter_value(4))
abutton5 = Button(root, text='5', padx=40, pady=20, command= lambda: enter_value(5))
abutton6 = Button(root, text='6', padx=40, pady=20, command= lambda: enter_value(6))
abutton7 = Button(root, text='7', padx=40, pady=20, command= lambda: enter_value(7))
abutton8 = Button(root, text='8', padx=40, pady=20, command= lambda: enter_value(8))
abutton9 = Button(root, text='9', padx=40, pady=20, command= lambda: enter_value(9))
abutton0 = Button(root, text='0', padx=40, pady=20, command= lambda: enter_value(0))

abuttoncomma = Button(root, text='.', padx=42, pady=20, command= lambda: enter_value('.'))
abuttonequal = Button(root, text='=', padx=40, pady=20, bg = 'green', command= lambda: equals())
abuttonclear = Button(root, text='clear', padx=80, pady=20, bg = 'red', command=clear)
abuttonadd = Button(root, text='+', padx=39, pady=20, command=add)
abuttonsubtract = Button(root, text='-', padx=41, pady=20, command= lambda: subtract('-'))
abuttonmultiply = Button(root, text='*', padx=41, pady=20, command=multiply)
abuttondivide = Button(root, text='/', padx=41, pady=20, command=divide)

#assemble the buttons
abutton7.grid(row = 1, column =0 )
abutton8.grid(row = 1, column =1 )
abutton9.grid(row = 1, column =2 )

abutton4.grid(row = 2 , column =0)
abutton5.grid(row = 2, column = 1)
abutton6.grid(row = 2, column = 2)

abutton1.grid(row = 3, column = 0)
abutton2.grid(row = 3, column = 1)
abutton3.grid(row = 3, column = 2)

abutton0.grid(row = 4, column = 0)
abuttonadd.grid(row = 4, column = 1)
abuttondivide.grid(row=4, column=2)

abuttonsubtract.grid(row=5, column=0)
abuttonmultiply.grid(row=5, column=1)
abuttoncomma.grid(row=5, column=2)

abuttonequal.grid(row = 6, column = 2)
abuttonclear.grid(row = 6, column =0, columnspan= 2 )

root.mainloop()
