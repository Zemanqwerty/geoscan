import cv2
from pioneer_sdk import Pioneer, Camera
import numpy as np

def load_coefficients(path):
    """ Loads camera matrix and distortion coefficients. """
    # FILE_STORAGE_READ
    cv_file = cv2.FileStorage(path, cv2.FILE_STORAGE_READ)

    # note we also have to specify the type to retrieve other wise we only get a
    # FileNode object back instead of a matrix
    camera_matrix = cv_file.getNode("mtx").mat()
    dist_matrix = cv_file.getNode("dist").mat()

    cv_file.release()
    return camera_matrix, dist_matrix

if __name__ == '__main__':
    camera_mtx, camera_dist = load_coefficients('data.yml')
    size_of_marker = 0.1  # side length in meters
    aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_1000)
    aruco_parameters = cv2.aruco.DetectorParameters_create()
    camera = Camera()
    mini = Pioneer()
    # Go to start point
    mini.arm()
    mini.takeoff()
    mini.go_to_local_point(x=0, y=0, z=1.5, yaw=0)
    while not mini.point_reached():
        pass
    send_manual_speed = False