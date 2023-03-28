import cv2
from django.http import StreamingHttpResponse
from django.shortcuts import render
from ultralytics import YOLO


# Create your views here.
def base(request):
    return render(request, "yoloweb/base.html")


def stream():
    model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)
    results = model('video.mp4', show=True, stream=True)  # List of Results objects

    for result, frame in results:
        # boxes = result[0].boxes.numpy()  # Boxes object for bbox outputs
        # for box in boxes:  # there could be more than one detection
        #     print("class", box.cls)
        #     print("xyxy", box.xyxy)
        #     print("conf", box.conf)

        ret, jpeg = cv2.imencode('.jpg', frame)

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n')

    # Destroy all the windows
    cv2.destroyAllWindows()


def video_feed(request):
    return StreamingHttpResponse(stream(), content_type='multipart/x-mixed-replace; boundary=frame')
