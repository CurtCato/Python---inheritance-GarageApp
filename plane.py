from vehicle import Vehicle

class Plane(Vehicle):

    def __init__(self):
        self.engine = "single"
        self.wing_span = "30 ft"
        Vehicle.__init__(self, "162 Skycatcher", "Cessna", 300, 500)

    def drive(self):
        print(f"The {self.manufacturer} {self.model} took off from the airway this morning with a 'buzz'!")

    def stop(self):
        print(f"The {self.manufacturer} {self.model} crashed after landing at {self.top_speed} mph.")

    def turn(self, direction):
        print(f"The {self.manufacturer} {self.model} exploded after turning {direction} at {self.top_speed} mph on the runway.")
