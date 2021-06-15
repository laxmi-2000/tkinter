from tkinter  import *
import random
import time

WIDTH=1500
HEIGHT=1000

tk=Tk()
canvas=Canvas(tk,width=WIDTH,height=HEIGHT)
tk.title("Bouncing Ball")
canvas.pack()

class Ball:
    def __init__(self, color, size):
        self.shape=canvas.create_oval(8,8,size, size, fill=color)
        self.xspeed=random.randrange(-8,8)
        self.yspeed=random.randrange(-8,8)
    def move(self):  
        canvas.move(self.shape,self.xspeed,self.yspeed)
        pos=canvas.coords(self.shape)
        if pos[3]>=HEIGHT or pos[1]<=0:
            self.yspeed=-self.yspeed
        if pos[2]>=WIDTH or pos[0]<=0:
            self.xspeed=-self.xspeed

colors=['red', 'spring green', 'green','yellow', 'grey', 'pink', 'purple', 'sky blue', 'black','dodgerblue','silver','orchid','teal','brown']

balls=[]
for i in range(100):
    balls.append(Ball(random.choice(colors),random.randrange(150,200)))

while True:
    for ball in balls:
        ball.move()
    tk.update()
    time.sleep(0.01)

tk.mainloop()
    
