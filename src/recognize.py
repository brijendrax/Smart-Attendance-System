import cv2
import time
from attendance import mark_attendance

exec(open('src/attendance.py').read())

recognizer = cv2.face.LBPHFaceRecognizer_create()

recognizer.read('trainer/trainer.yml')

faceCascade = cv2.CascadeClassifier(
    'models/haarcascade_frontalface_default.xml'
)

labels = {}

with open('trainer/labels.txt', 'r') as f:

    for line in f:

        id, name = line.strip().split(',')

        labels[int(id)] = name

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

marked = []

start_time = time.time()

while cam.isOpened():

    ret, img = cam.read()

    if not ret:

        print("Camera not working")
        break

    gray = cv2.cvtColor(
        img,
        cv2.COLOR_BGR2GRAY
    )

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5
    )

    for (x, y, w, h) in faces:

        id, confidence = recognizer.predict(
            gray[y:y+h, x:x+w]
        )

        if confidence < 45:

            name = labels[id]

            if name not in marked:

                mark_attendance(name)

                marked.append(name)

            text = f"{name} {round(confidence)}"

        else:

            text = "Unknown"

        cv2.rectangle(
            img,
            (x, y),
            (x+w, y+h),
            (0, 255, 0),
            2
        )

        cv2.putText(
            img,
            text,
            (x, y-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 255, 255),
            2
        )

    cv2.imshow(
        "Face Recognition Attendance",
        img
    )

    if time.time() - start_time >= 40:

        print("40 seconds completed")
        break

    if cv2.waitKey(1) & 0xFF == 27:

        print("ESC pressed")
        break

cam.release()

cv2.destroyAllWindows()

print("Attendance session ended")