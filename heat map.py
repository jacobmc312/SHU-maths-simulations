from tkinter import * 
from tkinter.ttk import *
from time import sleep
from random import randint, choice

direction = [1,2,3,4]

grid = []
for r in range(50):
    thisrow = []
    for c in range(70):
        thisrow.append(0)
    grid.append(thisrow)
for person in range(50):
    grid[randint(15,35)][randint(15,55)] = 1

heatmap = []
for r in range(50):
    thisrow = []
    for c in range(70):
        thisrow.append(-1)
    heatmap.append(thisrow)

heatmap[25][69] = 0
heatmap[25][0] = 0

for r in range(20,30):
    heatmap[r][67] = 1000

heatmap_max = 0
heatmapIncomplete = True
while heatmapIncomplete:
    for r in range(50):
        for c in range(70):
            if heatmap[r][c] == -1:
                if r-1>=0 and heatmap[r-1][c] == heatmap_max:
                    heatmap[r][c] = heatmap_max+1
                elif c-1>=0 and heatmap[r][c-1] == heatmap_max:
                    heatmap[r][c] = heatmap_max+1
                elif r+1<=49 and heatmap[r+1][c] == heatmap_max:
                    heatmap[r][c] = heatmap_max+1
                elif c+1<=69 and heatmap[r][c+1] == heatmap_max:
                    heatmap[r][c] = heatmap_max+1
    heatmap_max += 1

    heatmapIncomplete = False
    for row in heatmap:
        if -1 in row:
            heatmapIncomplete = True

window = Tk()
window.geometry('1400x1000')
window.title("Evacuation")
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
            if heatmap[r][c] == 0:
                colour = "red"
            elif grid[r][c] == 1:
                colour = "blue"
            elif heatmap[r][c] == 1000:
                colour = "black"
            else: 
                colour = "white"
            canvas.create_rectangle((20*c,20*r), (20*(c+1), 20*(r+1)), fill=colour)

    nextgrid = []
    for r in range(len(grid)):
        thisrow = []
        for c in range(len(grid[0])):
            thisrow.append(0)
        nextgrid.append(thisrow)

    for h in range(0,heatmap_max):
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if heatmap[r][c] == h:
                    if grid[r][c] == 1 and heatmap[r][c] > 1:
                        min_r = r
                        min_c = c
                        while direction:
                            d = choice(direction)
                            if r-1>=0 and heatmap[r-1][c] < heatmap[r][c] and d == 1:
                                min_r = r-1
                                min_c = c
                                direction.remove(1)
                            if c-1>=0 and heatmap[r][c-1] < heatmap[r][c] and d == 2:
                                min_r = r
                                min_c = c-1
                                direction.remove(2)
                            if r+1<=49 and heatmap[r+1][c] < heatmap[r][c] and d == 3:
                                min_r = r+1
                                min_c = c
                                direction.remove(3)
                            if c+1<=69 and heatmap[r][c+1] < heatmap[r][c] and d == 4:
                                min_r = r
                                min_c = c+1
                                direction.remove(4)
                        if nextgrid[min_r][min_c] == 0:
                            nextgrid[min_r][min_c] = 1
                            direction = [1,2,3,4]
                        else:
                            nextgrid[r][c] = 1
                            direction = [1,2,3,4]

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            grid[r][c] = nextgrid[r][c]
                        
    window.update()
    sleep(0.2)

window.mainloop()

