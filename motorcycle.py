from vehicle import Vehicle

class Motorcycle(Vehicle):

    def __init__(self):
        self.saddlebags = False
        self.wheels = 2
        Vehicle.__init__(self, "Street 750", "Harley Davidson", 180, 400)

    def drive(self):
        print(f"The {self.manufacturer} {self.model} drove by with a 'ROAR'!")

    def stop(self):
        print(f"The stuntman driving a {self.manufacturer} {self.model} made a jump at {self.top_speed} mph. Then he stopped.")

    def turn(self, direction):
        print(f"The {self.manufacturer} stuntman nearly flipped while turning {direction} at {self.top_speed} mph.")