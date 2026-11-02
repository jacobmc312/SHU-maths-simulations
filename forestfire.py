from tkinter import * 
from tkinter.ttk import *
from time import sleep
from random import randint, random, choice


wind = [N,S,E,W]

grid = []
for r in range(50):
    thisrow = []
    for c in range(70):
        thisrow.append(100)
    grid.append(thisrow)

grid[randint(15,35)][randint(15,55)] = 1

for b in range(10):
    bc = randint(0,69)
    br = randint(0,49)
    if grid[br][bc] != 1:
        grid[br][bc] = 10

window = Tk()
window.geometry('1400x1000')
window.title("Forest fire")
canvas = Canvas(window, width=1400, height=1000, bg='white')
canvas.pack(anchor=CENTER, expand=True)

def handler():
    global run
    run = False
    window.destroy()
window.protocol("WM_DELETE_WINDOW", handler)

direction = choice(wind)
print("Wind direction is",direction)

run = True

while run:
    canvas.delete("all")

    if random()<0.1:
        direction = choice(wind)
        print("Wind direction is",direction)
    
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 9:
                colour = "gray"
            elif grid[r][c] == 1:
                colour = "yellow"
            elif grid[r][c] == 2:
                colour = "orange"
            elif grid[r][c] == 3:
                colour = "red"
            elif grid[r][c] == 10:
                colour = "brown"
            else: 
                colour = "green"
            canvas.create_rectangle((20*c,20*r), (20*(c+1), 20*(r+1)), fill=colour)

    nextgrid = []

    for r in range(len(grid)):
        thisrow = []
        for c in range(len(grid[0])):
            i = 0.25
            thiscell = grid[r][c]
            if thiscell == 3:
                thiscell = 9
            if thiscell == 2:
                thiscell = 3
            if thiscell == 1:
                thiscell = 2
            elif thiscell == 100 and r-1>=0 and c-1>=0 and r+1<50 and c+1<70:
                if grid[r-1][c] <= 3:
                    if direction == "N":
                        i += 0.5
                    else:
                        i += 0.1
                elif grid[r][c-1] <= 3:
                    if direction == "E":
                        i += 0.5
                    else:
                        i += 0.1
                elif grid[r][c+1] <= 3:
                    if direction == "W":
                        i += 0.5
                    else:
                        i += 0.1
                elif grid[r+1][c] <= 3:
                    if direction == "S":
                        i += 0.5
                    else:
                        i += 0.1
                else:
                    i = 0
                if random()<i:
                    thiscell = 1
            elif thiscell == 10 and r-1>=0 and c-1>=0 and r+1<50 and c+1<70:
                if grid[r-1][c] <= 3:
                    if direction == "N":
                        i += 0.2
                    i += 0.1
                elif grid[r][c-1] <= 3:
                    if direction == "E":
                        i += 0.2
                    else:
                        i += 0.1
                elif grid[r][c+1] <= 3:
                    if direction == "W":
                        i += 0.2
                    else:
                        i += 0.1
                elif grid[r+1][c] <= 3:
                    if direction == "S":
                        i += 0.2
                    else:
                        i += 0.1
                else:
                    i = 0
                if random()<i:
                    thiscell = 1
                    print("building at",c,r,"is on fire.")
                    
            thisrow.append(thiscell)
        nextgrid.append(thisrow)

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            grid[r][c] = nextgrid[r+1][c+1]
        
        window.update()
        sleep(0.001)

window.mainloop()


