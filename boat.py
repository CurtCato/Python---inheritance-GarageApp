from vehicle import Vehicle

class Boat(Vehicle):

    def __init__(self):
        self.capacity = 8
        self.wake_size = "big"
        Vehicle.__init__(self, 80, "Pershing", 47, 4690)

    def drive(self):
        print(f"The {self.manufacturer} {self.model} flew by at {self.top_speed} with a splash.")


