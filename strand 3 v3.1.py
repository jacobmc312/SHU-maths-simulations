from tkinter import * 
from tkinter.ttk import *
from time import sleep
from random import randint, random, choice

grid = []
flood = []
blue = []
aqua = []

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
        amount = 20
        height = 25
        steepness = 1
        button.destroy()
        window_selection.destroy()
    elif mountain_level.get() == "Medium":
        amount = 10
        height = 35
        steepness = 4
        button.destroy()
        window_selection.destroy()
    elif mountain_level.get() == "Low":
        amount = 3
        height = 75
        steepness = 10
        button.destroy()
        window_selection.destroy()

    grid = terrain_builder(amount, height, steepness)

button = Button(window_selection, text="Begin Simulation", command=begin_button)
button.pack()

def terrain_builder(amount, height, steepness):
    
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
            
                if thiscell_terrain == 8 and random() < 0.1 / steepness:
                    thiscell_terrain = 9            
                elif thiscell_terrain == 7 and random() < 0.1 / steepness:
                    thiscell_terrain = 8            
                elif thiscell_terrain == 6 and random() < 0.1 / steepness:
                    thiscell_terrain = 7            
                elif thiscell_terrain == 5 and random() < 0.35 / steepness:
                    thiscell_terrain = 6            
                elif thiscell_terrain == 4 and random() < 0.4 / steepness:
                    thiscell_terrain = 5            
                elif thiscell_terrain == 3 and random() < 0.4 / steepness:
                    thiscell_terrain = 4            
                elif thiscell_terrain == 2 and random() < 0.5 / steepness:
                    thiscell_terrain = 3            
                elif thiscell_terrain == 1 and random() < 0.8 / steepness:
                    thiscell_terrain = 2

                elif thiscell_terrain == 100:
                    neighbourcell = [(r-1,c),(r,c-1),(r+1,c),(r,c+1)]
                    if any(0 <= rn < 50 and 0 <= cn < 70 and grid[rn][cn] <= 9 for rn, cn in neighbourcell):
                        if random() < 0.5: 
                            thiscell_terrain = 1
                                
                thisrow_terrain.append(thiscell_terrain)
            terrain.append(thisrow_terrain)
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                grid[r][c] = terrain[r][c]

    if random() > 0.5:
        if random() > 0.5:
            rs = 0
            cs = randint(0,69)
            grid[0][cs] = 1
        else:
            rs = randint(0,49)
            cs = 0
            grid[rs][0] = 1
    else:
        if random() > 0.5:
            rs = 49
            cs = randint(0,69)
            grid[49][cs] = 1
        else:
            rs = randint(0,49)
            cs = 69
            grid[rs][69] = 1

    window.update()
    floodbegin(rs, cs)
    return grid

def floodbegin(rs, cs):
    
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 1:
                colour = "lawngreen"
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
                colour = "lawngreen"
                grid[r][c] = 1
            canvas.create_rectangle((20*c,20*r), (20*(c+1), 20*(r+1)), fill=colour)
    
    run = True

    for r in range(50):
        blue_thisrow = []
        for c in range(70):
            blue_thisrow.append(0)
        blue.append(blue_thisrow)

    for r in range(50):
        aqua_thisrow = []
        for c in range(70):
            aqua_thisrow.append(0)
        aqua.append(aqua_thisrow)

    for r in range(50):
        flood_thisrow = []
        for c in range(70):
            flood_thisrow.append(0)
        flood.append(flood_thisrow)

    flood[rs][cs] = 1

    for i in range(1000):

        if random() < 0.05:
            watervalue = 1
        else:
            watervalue = 0
        
        new_flood = []
        
        for r in range(len(grid)):
            new_flood_thisrow = []
            for c in range(len(grid[0])):
                groundcell = grid[r][c]
                watercell = flood[r][c]

                if watercell + groundcell < 9 and watercell > 0:
                    watercell += watervalue
                    
                elif watercell == -1:
                    neighbourcell = [(r-1,c),(r,c-1),(r+1,c),(r,c+1)]
                    for rn, cn in neighbourcell:
                        if not(0 <= rn < 50 and 0 <= cn < 70):
                            neighbourcell.remove((rn,cn))
                        elif groundcell <= grid[rn][cn] or flood[rn][cn] > 0:
                            watercell = 1
                    
                elif watercell == 0:
                    neighbourcell = [(r-1,c),(r,c-1),(r+1,c),(r,c+1)]
                    if any(0 <= rn < 50 and 0 <= cn < 70 and flood[rn][cn] > 0 and groundcell < grid[rn][cn] + flood[rn][cn] and groundcell >= grid[rn][cn] for rn, cn in neighbourcell):
                        for rn, cn in neighbourcell:
                            if 0 <= rn < 50 and 0 <= cn < 70 and flood[rn][cn] > 0 and groundcell < grid[rn][cn] + flood[rn][cn] and groundcell >= grid[rn][cn]:
                                watercell = flood[rn][cn] + grid[rn][cn] - groundcell
                    elif any(0 <= rn < 50 and 0 <= cn < 70 and flood[rn][cn] > 0 and groundcell < grid[rn][cn] + flood[rn][cn] for rn, cn in neighbourcell):
                        watercell = -1
                    elif any(0 <= rn < 50 and 0 <= cn < 70 and flood[rn][cn] == -1 and groundcell < grid[rn][cn] for rn, cn in neighbourcell):
                        watercell = -1

                new_flood_thisrow.append(watercell)
            new_flood.append(new_flood_thisrow)
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                flood[r][c] = new_flood[r][c]
                                    
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if flood[r][c] > 1 and blue[r][c] == 0:
                    colour = "blue"
                    blue[r][c] = 1
                    canvas.create_rectangle((20*c,20*r), (20*(c+1), 20*(r+1)), fill=colour)
                elif (flood[r][c] == -1 or flood[r][c] == 1) and aqua[r][c] == 0 and blue[r][c] == 0:
                    colour = "aqua"
                    aqua[r][c] = 1
                    canvas.create_rectangle((20*c,20*r), (20*(c+1), 20*(r+1)), fill=colour)   
         
        window.update()
        sleep(0.01)
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 1:
                colour = "lawngreen"
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
                colour = "lawngreen"
                grid[r][c] = 1
            canvas.create_rectangle((20*c,20*r), (20*(c+1), 20*(r+1)), fill=colour)
    window.update()

window_selection.mainloop()
window.mainloop()

"""
Detect each cell that is eligable to flooding eg: every cell adjacent to a watercell that is not a watercell itself and is at a lower groundcell + watercell value

then add all these cells to a list that orders the heights and groups all the cells into quartiles eg: lower quartile has a 90% chance of spreading and higher quartile has 10%


"""

