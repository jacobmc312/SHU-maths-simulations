from tkinter import * 
from tkinter.ttk import *
from time import sleep
from random import randint, random, choice

grid = []

window = Tk()
window.geometry('1400x1000')
window.title("Simulation")
canvas = Canvas(window, width=1400, height=1000, bg='white')
canvas.pack(anchor=CENTER, expand=True)

window_selection = Toplevel(window)
window_selection.transient(window)
window_selection.geometry('300x150')
window_selection.title("Selection")

def handler():
    global run
    run = False
    window.destroy()
    window.protocol("WM_DELETE_WINDOW", handler)

mountain_level = Combobox(window_selection)
mountain_level['values'] = ("High","Medium","Low")
mountain_level.pack()

def begin_button():
    global grid
    
    if mountain_level.get() == "":
        message = Label(window_selection, text="Please select an option")
        message.pack()
        return
    
    if mountain_level.get() == "High":
        amount = 11
        height = 25
        button.destroy()
        window_selection.destroy()
    elif mountain_level.get() == "Medium":
        amount = 7
        height = 17
        button.destroy()
        window_selection.destroy()
    elif mountain_level.get() == "Low":
        amount = 3
        height = 15
        button.destroy()
        window_selection.destroy()

    grid = terrain_builder(amount, height)

button = Button(window_selection, text="Begin Simulation", command=begin_button)
button.pack()

def terrain_builder(amount, height):   
    
    for r in range(50):
        thisrow = []
        for c in range(70):
            thisrow.append(100)
        grid.append(thisrow)
        
    for i in range(amount): 
        grid[randint(0,49)][randint(0,69)] = 1

    for i in range(height):
        terrain = []
        
        for r in range(len(grid)):
            thisrow_terrain = []
            for c in range(len(grid[0])):
                thiscell_terrain = grid[r][c]
            
                if thiscell_terrain == 8 and random() < 0.1:
                    thiscell_terrain = 9            
                elif thiscell_terrain == 7:
                    thiscell_terrain = 8            
                elif thiscell_terrain == 6 and random() < 0.3:
                    thiscell_terrain = 7            
                elif thiscell_terrain == 5:
                    thiscell_terrain = 6            
                elif thiscell_terrain == 4:
                    thiscell_terrain = 5            
                elif thiscell_terrain == 3 and random() < 0.6:
                    thiscell_terrain = 4            
                elif thiscell_terrain == 2:
                    thiscell_terrain = 3            
                elif thiscell_terrain == 1:
                    thiscell_terrain = 2

                elif thiscell_terrain == 100 and r-1>=0 and c-1>=0 and r+1<50 and c+1<70:
                    if grid[r-1][c] <= 9 or grid[r][c-1] <= 9 or grid[r][c+1] <= 9 or grid[r+1][c] <= 9:
                        if random() > 0.2:
                            thiscell_terrain = 1
                        
                thisrow_terrain.append(thiscell_terrain)
            terrain.append(thisrow_terrain)
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                grid[r][c] = terrain[r][c]

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
                    colour = "lightgray"
                elif grid[r][c] == 8:
                    colour = "darkgray"
                elif grid[r][c] == 9:
                    colour = "dimgray"
                else:
                    colour = "blue"
                canvas.create_rectangle((20*c,20*r), (20*(c+1), 20*(r+1)), fill=colour)

    window.update()
    return grid

run = True

while run:
            
    nextgrid = []
    
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

window_selection.mainloop()
window.mainloop()
