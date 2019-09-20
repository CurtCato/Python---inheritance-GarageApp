from vehicle import Vehicle

class Truck(Vehicle):
    def __init__(self):
        self.wheels = 18
        Vehicle.__init__(self, "Classic XL", "Freightliner", 110, 700)

    def drive(self):
        print(f"An {self.wheels} wheeler, the {self.manufacturer} {self.model}, drove by with a 'Rattle'!")

    def stop(self):
        print(f"The {self.model} took forever to stop after driving at {self.top_speed} mph.")

    def turn(self, direction):
        print(f"The {self.model} nearly flipped while turning {direction} at {self.top_speed} mph.")