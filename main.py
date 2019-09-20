from boat import Boat
from vehicle import Vehicle
from corvette import Corvette
from motorcycle import Motorcycle
from plane import Plane
from truck import Truck

boat = Boat()
boat.drive()

vette = Corvette()
vette.drive()

moto = Motorcycle()
moto.drive()
moto.stop()
moto.turn("left")

plane = Plane()
plane.drive()
plane.stop()
plane.turn("right")

truck = Truck()
truck.drive()
truck.stop()
truck.turn("left")