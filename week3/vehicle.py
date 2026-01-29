class Vehicle():

    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

class Off_Road_Vehicle(Vehicle):
    def __init__(self,make,model,year,four_wheel_drive):
        Vehicle.__init__(self,make,model,year) 
        self.four_wheel_drive = four_wheel_drive

class SportCar(Vehicle):
    def __init__(self,make,model,year,max_speed):
        Vehicle.__init__(self,make,model,year)
        self.max_speed = max_speed

road = Off_Road_Vehicle("Toyota","Land Cruiser", 2020, True)
print(road.make)
print(road.model)
print(road.year)
print(road.four_wheel_drive)

spor = SportCar("Ferrari","488",2022,330)
print(spor.make)
print(spor.model)
print(spor.year)
print(spor.max_speed)