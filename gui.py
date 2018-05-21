from tkinter import *


def face_recognizer_gui():
    root = Tk()
    tag_frame = Frame(root)
    tag_frame.pack()
    tag_label = Label(tag_frame, text='Face Recognizer')

    tag_label.pack()
    root.mainloop()


face_recognizer_gui()
