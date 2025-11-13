class Engine:
    def __init__(self, horsepower):
       
        self.horsepower = horsepower
class Wheel:
    def __init__(self, size):
        self.size = size

class Car:
    def __init__(self, make, brand, horsepower, wheel_size):
        
        self.make = make
        self.brand = brand
    
        self.horsepower = Engine(horsepower)
      
        self.wheels = [Wheel(wheel_size) for _ in range(4)]
    
   
    def get_car(self):
        # We're getting the horsepower value from the Engine object
        hp = self.horsepower.horsepower
        # We're getting all wheel sizes from the list of Wheel objects
        wheel_sizes = [wheel.size for wheel in self.wheels]
        # We're returning a nice formatted string with all car details
        return f"make = {self.make}, brand = {self.brand}, horsepower = {hp}, wheel size = {wheel_sizes}"
    

# We're creating a new Car object with its details
car1 = Car("toyota", "corolla", 120, 16)
# We're printing out the car's information
print(car1.get_car())