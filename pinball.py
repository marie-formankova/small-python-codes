from tkinter import *
from tkinter import messagebox
import random

class Board:

    def __init__(self):
        self.root=Tk()
        self.root.geometry('550x600')
        self.platno=Canvas(self.root, width=500, height=500, bg = 'pink')
        self.platno.pack(pady=25)
        self.bouncer = self.platno.create_rectangle(235 , 495, 265, 500, width=10, fill = 'black')
        self.move_bouncer()
        self.start = Button(self.root, text = 'start', command = self.create_ball)    
        self.start.pack()   
        self.mx = None
        self.my = None
        

    def right(self, bouncer):
        self.platno.move(self.bouncer, 5, 0)
       
    def left(self, bouncer):
        self.platno.move(self.bouncer, -5, 0)
        
    def move_bouncer(self):
        self.root.bind('<Left>', self.left)
        self.root.bind('<Right>', self.right)

 
    def create_ball(self):
        self.ball=self.platno.create_oval(500, 150, 525, 175, fill = 'red')
        
        self.ball_move()

    def check_if_saved(self):
            self.boun_c = self.platno.coords(self.bouncer)
            bounceable = range(int(self.boun_c[0]),int(self.boun_c[2]))
            if int(self.ball_c[0]) in bounceable or int(self.ball_c[2]) in bounceable:
                return True
            else:
                print('you lose :(')
                return False

    def ball_move(self):
        rand_paces =  [1, 1.2, 1.4, 1.5, 1.7, 2, 2.5, 2.6, 2.7, 2.8, 3, 3.1, 3.2, 3.4, 3.6, 3.5, 3.6, 3.8, 3.9, 4, 4.1, 4.2,]
        self.ball_c = self.platno.coords(self.ball)
       
        
        if self.ball_c[0] <= 0:
            self.mx = random.choice(rand_paces)
        if self.ball_c[1]<=0:
            self.my = random.choice(rand_paces)
        if self.ball_c[2] >= 500:
            self.mx = -random.choice(rand_paces)
        if self.ball_c[3]>= 495:
            saved = self.check_if_saved()
            if saved == True:
                self.my = -random.choice(rand_paces)
            else:
                self.platno.delete(self.ball)
                
        
        
        try:
            self.platno.move(self.ball, self.mx, self.my)
        except:
            self.platno.move(self.ball, -3, 3)
        self.root.after(25, self.ball_move)


        


p=Board()

mainloop()