from exerciseFive.vehicle.bicycle import Bicycle
from exerciseFive.vehicle.car import Car


for vehicle in [Car(), Bicycle()]:
    print(vehicle.start_engine())
