from pioneer_sdk import Pioneer, Camera
import cv2
import math
import numpy as np

angle = float(0)
number_of_points = 10
increment = float(360 / number_of_points)
radius = 0.6
flight_height = float(1)

command_x = radius * math.cos(math.radians(angle))
command_y = radius * math.sin(math.radians(angle))
command_yaw = math.radians(angle)

first_point = True
last_point_reached = False

if __name__ == '__main__':
    print('start')
    pioneer_mini = Pioneer()
    pioneer_mini.arm()
    pioneer_mini.takeoff()
    camera = Camera()
    while True:
