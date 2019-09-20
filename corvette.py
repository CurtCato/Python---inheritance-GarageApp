from vehicle import Vehicle

class Corvette(Vehicle):

    def __init__(self):
        self.convertible = True
        Vehicle.__init__(self, "Corvette Stingray", "Chevrolette", 220, 460)

    def drive(self):
        print(f"This {self.model} flew by at {self.top_speed} with a flash!")