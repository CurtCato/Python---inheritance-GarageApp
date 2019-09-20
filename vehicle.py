# Practice: Custom Colors and Sounds
class Vehicle():

    def __init__(self, model, manufacturer, top_speed, hp):
        self.model = model
        self.manufacturer = manufacturer
        self.top_speed = top_speed
        self.horsepower = hp

    def drive(self):
        print(f"The vehicle went by with a 'zoooom!'")

    def stop(self):
        print(f"The vehicle came to a screeching stop.")

    def turn(self, direction):
        print(f"The vehicle turned left.")
