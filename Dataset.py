import cv2
import os
import psycopg2


def getLastID():
    try:
        abd = 0
        conns = psycopg2.connect(database="postgres", user="postgres", password="aniket", host="localhost",
                                 port="5432")
        curs = conns.cursor()
        query0 = "SELECT id FROM detail"
        curs.execute(query0)
        rown = curs.fetchall()
        for ro in rown:
            abd = ro
        conns.close()
        if abd:
            return abd[-1]
        else:
            return 0
    except:
        return 0


def insertDetail(ID, NAME, ENROLL, COURSE):
    getID = str(ID)
    getName = NAME
    getEnroll = ENROLL
    getCourse = COURSE
    conn = psycopg2.connect(database="postgres", user="postgres", password="aniket", host="localhost", port="5432")
    cursor = conn.cursor()
    query = "INSERT INTO detail VALUES ('" + getID + "','" + getName + "','" + getEnroll + "','" + getCourse + "')"
    cursor.execute(query)
    conn.commit()
    conn.close()


def createDataset():
    sample = 0
    face_cascade = cv2.CascadeClassifier("Cascade/Face.xml")
    getID = getLastID() + 1
    getName = input("Provide Name : ")
    getEnroll = input("Provide Enrollment No : ")
    getCourse = input("Provide Course (example: CSE,ME) : ")
    path = "Dataset/" + str(getID)
    if not os.path.exists(path):
        os.mkdir(path)
    insertDetail(getID, getName, getEnroll, getCourse)
    get_frame = cv2.VideoCapture(0)
    while True:
        _, frame = get_frame.read()
        frame = cv2.flip(frame, 1)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face_tuple = face_cascade.detectMultiScale(gray, 1.2, 5, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)
        for (x, y, w, h) in face_tuple:
            cv2.imwrite("Dataset/" + str(getID) + "/" + "User." + str(getID) + "." + str(sample) + ".jpg",
                        gray[y:y + h, x:x + w])
            sample += 1
        if sample >= 21:
            get_frame.release()
            cv2.destroyAllWindows()
            break


createDataset()
