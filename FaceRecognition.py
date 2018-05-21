import cv2
import psycopg2
from mail_configuration import send_notifications
import threading
import time


def getDetails(idss):
    conn = psycopg2.connect(database="postgres", user="postgres", password="aniket", host="localhost", port="5432")
    cur = conn.cursor()
    query = "SELECT * FROM detail WHERE id=" + str(idss)
    cur.execute(query)
    row = cur.fetchall()
    for rows in row:
        profile = rows
    conn.close()
    return profile


face_cascade = cv2.CascadeClassifier("Cascade/Face.xml")
rec = cv2.face.LBPHFaceRecognizer_create()
rec.read("Trainer/Trainer.yml")
video = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_COMPLEX_SMALL


def recognizer():
    while True:
        sample = 0
        thread = None
        _, frame = video.read()
        frame = cv2.flip(frame, 1)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face_tuple = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100),
                                                   flags=cv2.CASCADE_SCALE_IMAGE)
        for (x, y, w, h) in face_tuple:
            ids, con = rec.predict(gray[y:y + h, x:x + w])
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 44, 36), 2)

            if con < 70:
                a = getDetails(ids)
                cv2.putText(frame, str(a[1]), (x, y + h + 20), font, 1, (255, 255, 255), 1)
                cv2.putText(frame, str(a[2]), (x, y + h + 40), font, 1, (255, 255, 255), 1)
                cv2.putText(frame, str(a[3]), (x, y + h + 60), font, 1, (255, 255, 255), 1)
            else:
                cv2.putText(frame, "Unknown " + str(con), (x, y + h + 20), font, 1, (255, 255, 255), 1)
                cv2.imwrite("Unknown Person/" + "unknown" + str(sample) + ".jpg", frame[y:y + h, x:x + w])
                sample += 1
                if thread is None:
                    thread = threading._start_new_thread(send_notifications, ())
        resize = cv2.resize(frame, (640, 480))
        # resize = cv2.resize(frame, (1366, 768))
        cv2.imshow("Face Recognizer", resize)
        if cv2.waitKey(1) == ord('q'):
            video.release()
            cv2.destroyAllWindows()
            break


recognizer()
