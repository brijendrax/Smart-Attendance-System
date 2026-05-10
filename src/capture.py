import cv2
import os

import sys

if len(sys.argv) > 1:

    name = sys.argv[1]

else:

    name = input("Enter Student Name: ")

path = f"dataset/{name}"

os.makedirs(path, exist_ok=True)

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

face_detector = cv2.CascadeClassifier(
    'models/haarcascade_frontalface_default.xml'
)

count = 0

while True:

    ret, img = cam.read()

    if not ret:
        print("Failed to capture image")
        break

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:

        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

        count += 1

        cv2.imwrite(
            f"{path}/{count}.jpg",
            gray[y:y+h, x:x+w]
        )

        cv2.putText(
            img,
            str(count),
            (x, y-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

    cv2.imshow("Capture Faces", img)

    k = cv2.waitKey(1)

    if k == 27:
        break

    elif count >= 300:
        break

print("Face samples captured successfully")

cam.release()
cv2.destroyAllWindows()