import cv2
import os
import numpy as np
from PIL import Image

path = 'dataset'

recognizer = cv2.face.LBPHFaceRecognizer_create()

detector = cv2.CascadeClassifier(
    'models/haarcascade_frontalface_default.xml'
)

faces = []
ids = []
label_ids = {}

current_id = 0

for person_name in os.listdir(path):

    person_path = os.path.join(path, person_name)

    if not os.path.isdir(person_path):
        continue

    label_ids[current_id] = person_name

    for image_name in os.listdir(person_path):

        image_path = os.path.join(person_path, image_name)

        pil_img = Image.open(image_path).convert('L')

        img_numpy = np.array(pil_img, 'uint8')

        detected_faces = detector.detectMultiScale(img_numpy)

        for (x, y, w, h) in detected_faces:

            faces.append(img_numpy[y:y+h, x:x+w])

            ids.append(current_id)

    current_id += 1

recognizer.train(faces, np.array(ids))

recognizer.save('trainer/trainer.yml')

with open('trainer/labels.txt', 'w') as f:

    for key, value in label_ids.items():

        f.write(f"{key},{value}\n")

print("Model trained successfully")