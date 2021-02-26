from tkinter import *

class arrows:
    def __init__(self):
        self.o=Tk()
        self.w=400
        self.h=400
        self.x=self.w//2
        self.y=self.h//2
        self.platno=Canvas(self.o, width=self.w, height=self.h)
        self.platno.pack()
        self.kolecko=self.platno.create_oval(self.x, self.y, self.x+10, self.y+10, fill = 'lime green')
        def left(s):
            self.x=-10
            self.y=0
            self.platno.move(self.kolecko, self.x, self.y)
        def right(s):
            x=10
            y=0
            self.platno.move(self.kolecko, x, y)
        def down(s):
            x=0
            y=10
            self.platno.move(self.kolecko, x, y)
        def up(s):
            x=0
            y=-10
            self.platno.move(self.kolecko, x, y)
        def posun(self):
            self.o.bind('<Left>', left)
            self.o.bind('<Right>', right)
            self.o.bind('<Down>', down)
            self.o.bind('<Up>', up)
        self.p=posun(self)

a=arrows()
mainloop()