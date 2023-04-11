# from pioneer_sdk import Pioneer, Camera
import cv2
import numpy as np
import time

if __name__ == '__main__':
    print('''
    1 -- arm
    2 -- disarm
    3 -- takeoff
    4 -- land
    ↶q  w↑  e↷    i-↑
    ←a      d→     k-↓
        s↓''')
    pioneer_mini = Pioneer()
    camera = Camera()
    min_v = 1300
    max_v = 1700
    while True:
        ch_1 = 1500
        ch_2 = 1500
        ch_3 = 1500
        ch_5 = 2000
        ch_4 = 1500
        frame = camera.get_frame()
        if frame is not None:
            camera_frame = cv2.imdecode(np.frombuffer(camera.get_frame(), dtype=np.uint8),
                                    cv2.IMREAD_COLOR)
            cv2.imshow('pioneer_camera_stream', camera_frame)
        key = cv2.waitKey(1)
        if key == 27:  # esc
            print('esc pressed')
            cv2.destroyAllWindows()
            pioneer_mini.land()
            break
        elif key == ord('1'):
            pioneer_mini.arm()
        elif key == ord('2'):
            pioneer_mini.disarm()
        elif key == ord('3'):
            time.sleep(1)
            pioneer_mini.takeoff()
            time.sleep(2)
        elif key == ord('4'):
            time.sleep(2)
            pioneer_mini.land()
            time.sleep(2)