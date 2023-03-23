import cv2

video = cv2.VideoCapture('22_ccPWL6dq.mp4')
if not video.isOpened():
    print("Error opening video file")

frame_skip_interval = 4
fps=int(video.get(cv2.CAP_PROP_FPS))

while True:
    ret, frame = video.read()

    if not ret:
        break

    cv2.imshow('Video', frame)
    cv2.waitKey(1)

    for i in range(0,fps,frame_skip_interval):
        video.grab()

video.release()
cv2.destroyAllWindows()
