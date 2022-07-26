import time
from modules.sensor_controller import SensorController

# Do NOT change this script
sensor_controller = SensorController()
sensor_controller.track_rod()
print("Distance: ", sensor_controller.get_distance())
print("Shape from distance: ", sensor_controller.get_shape_from_distance())
