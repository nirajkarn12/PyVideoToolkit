import cv2
import os
import time


cam = cv2.VideoCapture(r"C:\Users\niraz\PycharmProjects\image_watermark\video2.mp4")


if not os.path.exists('data'):
    os.makedirs('data')


total_duration = 20
interval = 5


num_frames = total_duration // interval


for current_frame in range(num_frames):

    time.sleep(interval)


    ret, frame = cam.read()

    if not ret:
        break


    name = f'./data/frame{current_frame + 1}.jpg'
    print(f'Creating: {name}')
    cv2.imwrite(name, frame)


cam.release()
cv2.destroyAllWindows()
