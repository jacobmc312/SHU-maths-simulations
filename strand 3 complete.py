from tkinter import * 
from tkinter.ttk import *
from time import sleep
from random import randint, random, choice, shuffle
import numpy as np
import matplotlib.pyplot as plt

grid = []
flood = []
blue = []
aqua = []
heatmap = []
heatmap_25 = []

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

Label1 = Label(window_selection, text = "Select Terrain Height")
Label1.pack()

mountain_level = Combobox(window_selection)
mountain_level['values'] = ("High","Medium","Low")
mountain_level.pack()

Label2 = Label(window_selection, text = "Select How Many Iterations")
Label2.pack()

monte_carlo = Combobox(window_selection)
monte_carlo['values'] = ("100(≈1min 30s)","1000(≈15min)")
monte_carlo.pack()

def begin_button():
    global grid
    
    if mountain_level.get() == "" or monte_carlo.get() == "":
        message = Label(window_selection, text="Please select an option")
        message.pack()
        return
    if monte_carlo.get() == "100(≈1min 30s)":
        iterations = 100
        if mountain_level.get() == "High":
            amount = 20
            height = 25
            steepness = 1
            button.destroy()
            window_selection.withdraw()
        elif mountain_level.get() == "Medium":
            amount = 10
            height = 35
            steepness = 4
            button.destroy()
            window_selection.withdraw()
        elif mountain_level.get() == "Low":
            amount = 3
            height = 75
            steepness = 10
            button.destroy()
            window_selection.withdraw()
    elif monte_carlo.get() == "1000(≈15min)":
        iterations = 1000
        if mountain_level.get() == "High":
            amount = 20
            height = 25
            steepness = 1
            button.destroy()
            window_selection.withdraw()
        elif mountain_level.get() == "Medium":
            amount = 10
            height = 35
            steepness = 4
            button.destroy()
            window_selection.withdraw()
        elif mountain_level.get() == "Low":
            amount = 3
            height = 75
            steepness = 10
            button.destroy()
            window_selection.withdraw()
            
    grid = terrain_builder(amount, height, steepness, iterations)

button = Button(window_selection, text="Begin Simulation", command=begin_button)
button.pack()

def floodloop(iterations):

    for r in range(50):
        heatmap_thisrow = []
        for c in range(70):
            heatmap_thisrow.append(0)
        heatmap.append(heatmap_thisrow)

    for r in range(50):
        heatmap_25_thisrow = []
        for c in range(70):
            heatmap_25_thisrow.append(0)
        heatmap_25.append(heatmap_25_thisrow)

    flooded_heights = [0,0,0,0,0,0,0,0,0]
    flooded_heights_percent = []
    flooded_heights_chart = []
    grid_heights = [0,0,0,0,0,0,0,0,0]
    grid_heights_chart = []

    for r in range(len(grid)):
            for c in range(len(grid[0])):
                gcell = grid[r][c]
                grid_heights[gcell-1] += 1

    for i in range(iterations):

        flood = []

        total = 1
        
        for r in range(50):
            flood_thisrow = []
            for c in range(70):
                flood_thisrow.append(0)
            flood.append(flood_thisrow)

        if random() > 0.5:
            if random() > 0.5:
                rs = 0
                cs = randint(0,69)
            else:
                rs = randint(0,49)
                cs = 0
        else:
            if random() > 0.5:
                rs = 49
                cs = randint(0,69)
            else:
                rs = randint(0,49)
                cs = 69

        flood[rs][cs] = 1
                
        while total < 1500:
            
            spread = []
            
            for r in range(len(grid)):
                for c in range(len(grid[0])):
                    groundcell = grid[r][c]
                    watercell = flood[r][c]
                    
                    if watercell == 0:
                        neighbourcell = [(r-1,c),(r,c-1),(r+1,c),(r,c+1)]
                        if any(0 <= rn < 50 and 0 <= cn < 70 and flood[rn][cn] >= 1 for rn, cn in neighbourcell):
                            spread.append((groundcell,r,c))

            shuffle(spread)
            spread.sort(key=lambda x: x[0])

            n = (len(spread))

            q1, q2, q3, q4, q5 = n // 8, n // 4, (n * 3) // 8, n // 2, (n * 5) // 8

            batches = [(spread[:q1], 0.95), (spread[q1:q2], 0.05), (spread[q2:q3], 0.03), (spread[q3:q4], 0.01), (spread[q4:q5], 0.005)]

            for batch, probability in batches:
                for g, r, c in batch:
                    if random() < probability:
                        flood[r][c] = 1
                        flooded_heights[g-1] += 1
                        total += 1
        print(i+1)
        
        for r in range(len(heatmap)):
            for c in range(len(heatmap[0])):
                heatcell = heatmap[r][c]
                heatmap[r][c] = heatcell + flood[r][c]

    for avg in range(len(grid_heights)):
        flooded_heights_chart.append(flooded_heights[avg]/iterations)
        grid_heights_chart.append(grid_heights[avg]-(flooded_heights[avg]/iterations))
        if grid_heights[avg] != 0:
            flooded_heights_percent.append(flooded_heights[avg]/(grid_heights[avg]*(iterations/100)))
        else:
            flooded_heights_percent.append(0)

    window_heatmap = Toplevel(window)
    window_heatmap.transient(window)
    window_heatmap.geometry('700x770')
    window_heatmap.title("Heatmap")
    canvas_heatmap = Canvas(window_heatmap, width=700, height=770, bg='white')
    canvas_heatmap.pack(anchor=CENTER, expand=True)

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 2:
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
                
            canvas_heatmap.create_rectangle((5*c,5*r), (5*(c+1), 5*(r+1)), fill=colour)

    canvas_heatmap.create_rectangle((360,5), (387,32), fill="lawngreen")
    canvas_heatmap.create_rectangle((360,32), (387,59), fill="lime")
    canvas_heatmap.create_rectangle((360,59), (387,86), fill="limegreen")
    canvas_heatmap.create_rectangle((360,86), (387,113), fill="forestgreen")
    canvas_heatmap.create_rectangle((360,113), (387,140), fill="green")
    canvas_heatmap.create_rectangle((360,140), (387,167), fill="darkgreen")
    canvas_heatmap.create_rectangle((360,167), (387,194), fill="lightgray")
    canvas_heatmap.create_rectangle((360,194), (387,221), fill="darkgray")
    canvas_heatmap.create_rectangle((360,221), (387,248), fill="dimgray")

    canvas_heatmap.create_text(410,18, text="0-10m")
    canvas_heatmap.create_text(415,45, text="10-20m")
    canvas_heatmap.create_text(415,72, text="20-30m")
    canvas_heatmap.create_text(415,99, text="30-40m")
    canvas_heatmap.create_text(415,126, text="40-50m")
    canvas_heatmap.create_text(415,153, text="50-60m")
    canvas_heatmap.create_text(415,180, text="60-70m")
    canvas_heatmap.create_text(415,207, text="70-80m")
    canvas_heatmap.create_text(415,234, text="80-90m")

    canvas_heatmap.create_text(475,18, font="times 12 bold", text="Original Terrain Map", anchor="nw")

    canvas_heatmap.create_text(450,45, font="times 8", text="This is a 1/8th scale copy of the original\nterrain map, shown in the simulation it's\nhelpful for comparisons to the heatmap below.", anchor="nw")
    

    for r in range(len(heatmap)):
        for c in range(len(heatmap[0])):
            if heatmap[r][c] <= 25*(iterations/100):
                colour = "lime"
                heatmap_25[r][c] = 1
            elif 25 < heatmap[r][c] <= 50*(iterations/100):
                colour = "yellow"
            elif 50 < heatmap[r][c] <= 75*(iterations/100):
                colour = "orange"
            else:
                colour = "red"
                                
            canvas_heatmap.create_rectangle((5*c,260+(5*r)), (5*(c+1), 260+(5*(r+1))), fill=colour)

    canvas_heatmap.create_rectangle((360,265), (387,292), fill="lime")
    canvas_heatmap.create_rectangle((360,292), (387,319), fill="yellow")
    canvas_heatmap.create_rectangle((360,319), (387,346), fill="orange")
    canvas_heatmap.create_rectangle((360,346), (387,373), fill="red")

    canvas_heatmap.create_text(405,278, text="0-25%")
    canvas_heatmap.create_text(408,305, text="25-50%")
    canvas_heatmap.create_text(408,332, text="50-75%")
    canvas_heatmap.create_text(410,359, text="75-100%")

    canvas_heatmap.create_text(475,278, font="times 12 bold", text="Flood Heatmap", anchor="nw")

    canvas_heatmap.create_text(450,305, font="times 8", text=f"This is a heatmap of the most flooded areas,\nwhere each colour represents a different\nlevel of flooding eg:(a lime cell is a cell\nthat has been flooded in 25% or less of the\n{iterations} iterations of the simulation).", anchor="nw")
    
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if heatmap_25[r][c] == 1:
                if grid[r][c] == 2:
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
            else:
                colour = "blue"
                    
            canvas_heatmap.create_rectangle((5*c,520+(5*r)), (5*(c+1), 520+(5*(r+1))), fill=colour)
    
    canvas_heatmap.create_rectangle((360,525), (387,552), fill="blue")

    canvas_heatmap.create_text(410,538, text="25-100%")

    canvas_heatmap.create_text(475,538, font="times 12 bold", text="Flood Safe Map", anchor="nw")

    canvas_heatmap.create_text(450,565, font="times 8", text=f"This is a map of the cells that survived 75%\nor more of the {iterations} iterations.", anchor="nw")

    window_heatmap.update()

    xaxis = ["0-10m","10-20m","20-30m","30-40m","40-50m","50-60m","60-70m","70-80m","80-90m"]

    plt.bar(xaxis, grid_heights_chart, color="green")
    flood_bar = plt.bar(xaxis, flooded_heights_chart, bottom=grid_heights_chart, color="blue")
    plt.legend(["Not Flooded","Flooded"])
    plt.title("Flood Percentage per Height")
    plt.xlabel("Terrain Heights")
    plt.ylabel("Total Cells")
    k = 0
    for rect in flood_bar:
        size = rect.get_height() + grid_heights_chart[k]
        label = f"{round(flooded_heights_percent[k], 2)}%"
        plt.text(rect.get_x() + rect.get_width() / 2.0, size, label, ha='center', va='bottom')
        k += 1
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
    
def terrain_builder(amount, height, steepness, iterations):
    
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

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 2:
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
    floodbegin(iterations)
    
    return grid

def floodbegin(iterations):

    run = True

    if random() > 0.5:
        if random() > 0.5:
            rs = 0
            cs = randint(0,69)
        else:
            rs = randint(0,49)
            cs = 0
    else:
        if random() > 0.5:
            rs = 49
            cs = randint(0,69)
        else:
            rs = randint(0,49)
            cs = 69

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
    total = 1

    while total < 1500 and run:
        
        spread = []
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                groundcell = grid[r][c]
                watercell = flood[r][c]
                
                if watercell == 0:
                    neighbourcell = [(r-1,c),(r,c-1),(r+1,c),(r,c+1)]
                    if any(0 <= rn < 50 and 0 <= cn < 70 and flood[rn][cn] >= 1 for rn, cn in neighbourcell):
                        spread.append((groundcell,r,c))

        shuffle(spread)
        spread.sort(key=lambda x: x[0])

        n = (len(spread))

        q1, q2, q3, q4, q5 = n // 8, n // 4, (n * 3) // 8, n // 2, (n * 5) // 8

        batches = [(spread[:q1], 0.95), (spread[q1:q2], 0.05), (spread[q2:q3], 0.03), (spread[q3:q4], 0.01), (spread[q4:q5], 0.005)]

        for batch, probability in batches:
            for _, r, c in batch:
                if random() < probability:
                    flood[r][c] = 1
                    total += 1
                                    
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if flood[r][c] == 2 and blue[r][c] == 0:
                    colour = "blue"
                    blue[r][c] = 1
                    canvas.create_rectangle((20*c,20*r), (20*(c+1), 20*(r+1)), fill=colour)
                elif flood[r][c] == 1 and aqua[r][c] == 0:
                    colour = "aqua"
                    aqua[r][c] = 1
                    flood[r][c] = 2
                    canvas.create_rectangle((20*c,20*r), (20*(c+1), 20*(r+1)), fill=colour)

        window.update()
        sleep(0.01)

    for r in range(len(grid)):
            for c in range(len(grid[0])):
                if flood[r][c] == 2 and blue[r][c] == 0:
                    colour = "blue"
                    canvas.create_rectangle((20*c,20*r), (20*(c+1), 20*(r+1)), fill=colour)
                    
    window.update()
    floodloop(iterations)
window_selection.mainloop()
window.mainloop()



