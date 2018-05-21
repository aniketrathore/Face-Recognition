import os
import cv2
import numpy as np
from PIL import Image
import io

recognizer = cv2.face.LBPHFaceRecognizer_create()
faceDetect = cv2.CascadeClassifier("Cascade/Face.xml")
path = "Dataset"


def imageTrainer():
    image_list = []
    list1 = []
    for fn in os.listdir(path):
        list1.append(os.path.join(path, fn))
    for pt in range(0, len(list1)):
        for pt1 in os.listdir(list1[pt]):
            image_list.append(os.path.join(list1[pt], pt1))
    face = []
    Ids = []
    for images in image_list:
        PIL_Image = Image.open(images).convert('L')
        ImageNP = np.array(PIL_Image)
        ID = int(os.path.split(images)[-1].split(".")[1])
        faces = faceDetect.detectMultiScale(ImageNP)
        for (x, y, w, h) in faces:
            face.append(ImageNP[y:y + h, x:x + w])
            Ids.append(ID)

    recognizer.train(face, np.array(Ids))
    recognizer.write("Trainer/Trainer.yml")
    cv2.destroyAllWindows()


imageTrainer()
