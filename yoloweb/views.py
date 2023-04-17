from django.http import StreamingHttpResponse
from django.shortcuts import render
import cv2
from ultralytics import YOLO


def base(request):
    return render(request, 'yoloweb/index.html')


def stream():
    model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)
    results = model('video.mp4', show=True, stream=True)  # List of Results objects

    for result, frame in results:
        w, h, c = frame.shape
        frame = cv2.resize(frame, (int(h/2), int(w/2)), interpolation=cv2.INTER_LINEAR)
        ret, jpeg = cv2.imencode('.jpg', frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n')

    # Destroy all the windows
    cv2.destroyAllWindows()


def video_feed(request):
    return StreamingHttpResponse(stream(), content_type='multipart/x-mixed-replace; boundary=frame')