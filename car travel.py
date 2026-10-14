import random
from random import randint
import matplotlib.pyplot as plt

cars = []
junctions = [0,10,20,30,40,50,60,70,80,90]
sjunctions = [10,20,30,40,50,60,70,80,90,100]
car_amount = 0
number = 0
Time = []
Totalcars = []

class car:
    def __init__(self, colour, start, destination, direction, number):
        self.colour = colour
        self.location = start
        self.destination = destination
        self.direction = direction
        self.number = number
        self.join()
        
    def join(self):
        global cars
        cars.append(self)

    def move(self):
        if self.direction == "North":
            self.location += 1
        else:
            self.location -= 1
        if self.location == self.destination:
            self.leave()

    def leave(self):
        global cars
        cars.remove(self)

    def report(self):
        print(f"{self.colour} car at {self.location}, heading for {self.destination}, going {self.direction}, No:{self.number}")

    @classmethod
    def addcar(self):
        for i in range(randint(0,10)):
            colour = ["Blue","Red","Yellow","Green","Silver","Orange","Purple"]
            if randint(0,1) == 0:
                a = random.choice(junctions)
                exits = list(range(a+10,101,10))
                b = random.choice(exits)
                direction = "North"
            else:
                a = random.choice(sjunctions)
                exits = list(range(-1,a-10,10))
                b = random.choice(exits) + 1
                direction = "South"
            if not any((car.location == a and car.direction == direction) for car in cars):
                global number
                number += 1
                self(random.choice(colour),a,b,direction,number)

t = 0
car.addcar()

while t <= 200:
    if randint(0,1) == 0 and car_amount <= 100:
        car.addcar()
    for car in cars:
        car.move()
        #car.report()
    t += 1
    car_amount = len(cars)
    Time.append(t)
    Totalcars.append(car_amount)
    #print("There are",car_amount,"cars.")

print(f"There have been {car.number} individual cars on the road.")
plt.plot(Time,Totalcars)
plt.xlabel('Time')
plt.ylabel('No. Cars')
plt.show()

