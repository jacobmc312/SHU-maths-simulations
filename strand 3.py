from tkinter import * 
from tkinter.ttk import *
from time import sleep
from random import randint, random, choice

window = Tk()
window.geometry('1400x1000')
window.title("Selection")
canvas = Canvas(window, width=1400, height=1000, bg='white')
message = Label(window, text="Select a simulation")
message.pack()
canvas.pack(anchor=CENTER, expand=True)


def handler():
    global run
    run = False
    window.destroy()
window.protocol("WM_DELETE_WINDOW", handler)

grid = []
for r in range(50):
    thisrow = []
    for c in range(70):
        thisrow.append(randint(0,10))
    grid.append(thisrow)

for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == 1:
            colour = "chartreuse"
        elif grid[r][c] == 2:
            colour = "lime"
        elif grid[r][c] == 3:
            colour = "limegreen"
        elif grid[r][c] == 4:
            colour = "forestgreen"
        elif grid[r][c] == 5:
            colour = "green"
        elif grid[r][c] == 6:
            colour = "darkgreen"
        elif grid[r][c] == 7:
            colour = "dimgray"
        elif grid[r][c] == 8:
            colour = "darkgray"
        elif grid[r][c] == 9:
            colour = "lightgray"
        else:
            colour = "blue"
        canvas.create_rectangle((20*c,20*r), (20*(c+1), 20*(r+1)), fill=colour)

run = True

while run:
            
    nextgrid = []
    
    if random()>0.1:
        for r in range(len(grid)):
            thisrow = []
            for c in range(len(grid[0])):
                thiscell = grid[r][c]
                thiscell -= 1
                thisrow.append(thiscell)
                if thiscell == 0:
                    canvas.create_rectangle((20*c,20*r), (20*(c+1), 20*(r+1)), fill="blue")
            nextgrid.append(thisrow)
                
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                grid[r][c] = nextgrid[r][c]

    window.update()
    sleep(0.2)

window.mainloop()
