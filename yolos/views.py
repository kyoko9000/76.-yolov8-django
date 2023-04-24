import threading

from django.http import StreamingHttpResponse
from django.shortcuts import render
import cv2
from ultralytics import YOLO


def base(request):
    return render(request, 'yolos/index1.html')


def stream(link):
    print("process: ", link)
    model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)
    results = model(link, show=True, stream=True)  # List of Results objects

    for result, frame in results:
        w, h, c = frame.shape
        frame = cv2.resize(frame, (int(h / 3), int(w / 3)), interpolation=cv2.INTER_LINEAR)
        ret, jpeg = cv2.imencode('.jpg', frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n')

    # Destroy all the windows
    cv2.destroyAllWindows()


def video_feed(request):
    return StreamingHttpResponse(stream('video.mp4'), content_type='multipart/x-mixed-replace; boundary=frame')


def video_feed_1(request):
    return StreamingHttpResponse(stream('video1.mp4'), content_type='multipart/x-mixed-replace; boundary=frame')
