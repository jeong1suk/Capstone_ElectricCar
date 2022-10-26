import cv2
import os

#print(cv2.__version__)

filepath = 'data/PETS2000.avi'
video = cv2.VideoCapture(filepath)

if not video.isOpened():
    print("Could not Open : ", filepath)
    exit(0)

length = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = video.get(cv2.CAP_PROP_FPS)

print("length: ", length) # 1452
print("width: ", width) # 352
print("height: ", height) # 288
print("fps: ", fps) # 25.0

# try:
#     if not os.path.exists(filepath[:-4]):
#         os.makedirs(filepath[:-4])
# except OSError:
#     print('Error: Creating directory. ' + filepath[:-4])

# count = 0

# while(video.isOpened()):
#     ret, image = video.read()
#     if (int(video.get(1)) % fps == 0):
#         cv2.imwrite(filepath[:-4] + "/frame%d.jpg" % count, image)
#         print('Saved frame number :', str(int(video.get(1))))
#         count += 1

# video.release()