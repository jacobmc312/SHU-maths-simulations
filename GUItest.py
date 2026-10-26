from tkinter import * 
from tkinter.ttk import *

gui = Tk()

gui.title("HI")
gui.geometry("300x150")
gui.configure(background="chartreuse")
message = Label(gui, text="THIS IS GREEN")
message.pack()

def do_when_clicked():
    gui.configure(background="blue")
    message.config(text="THIS IS BLUE")
    button.destroy()
    
button = Button(gui, text="Click me", command=do_when_clicked)
button.pack()

message3 = Label(gui, text="What's your name?")
message3.pack()

txt = Entry(gui)
txt.pack()

def do_when_clicked2(): 
    name = txt.get()
    message3.config(text=f"Beam me up, {name}!")
    txt.destroy()
    button2.destroy()

button2 = Button(gui, text="Enter", command=do_when_clicked2)
button2.pack()

combo = Combobox(gui)
combo['values'] = ("Doc", "Happy", "Sneezy", "Sleepy", "Bashful", "Grumpy", "Dopey")
combo.pack()

current_value = combo.get()

gui.mainloop()
