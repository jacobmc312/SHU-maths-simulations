from tkinter import * 
from tkinter.ttk import *
from time import sleep
from random import randint

grid = []
for r in range(50):
    thisrow = []
    for c in range(70):
        thisrow.append(randint(0,1))
    grid.append(thisrow)

window = Tk()
window.geometry('1400x1000')
window.title("Game of Life")
canvas = Canvas(window, width=1400, height=1000, bg='white')
canvas.pack(anchor=CENTER, expand=True)

def handler():
    global run
    run = False
    window.destroy()
window.protocol("WM_DELETE_WINDOW", handler)

run = True

while run:
    canvas.delete("all")

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 1:
                colour = "blue"
            else: 
                colour = "white"
            canvas.create_rectangle((20*c,20*r), (20*(c+1), 20*(r+1)), fill=colour)

    window.update()
    sleep(0.5)

    nextgrid = []

    for r in range(len(grid)):
        thisrow = []
        for c in range(len(grid[0])):
            thiscell = grid[r][c]
            if r-1>=0 and c-1>=0 and r+1<50 and c+1<70:
                thissum = grid[r-1][c-1] + grid[r-1][c] + grid[r-1][c+1] + grid[r][c-1] + grid[r][c+1] + grid[r+1][c-1] + grid[r+1][c] + grid[r+1][c+1]

                if thissum == 1 or (thissum < 2 or thissum > 3):
                    thiscell = 0
                elif thissum == 3:
                    thiscell = 1
            else: 
                thiscell = 0
            thisrow.append(thiscell)
        nextgrid.append(thisrow)

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            grid[r][c] = nextgrid[r][c]
    window.update()
    sleep(0.5)

window.mainloop()
