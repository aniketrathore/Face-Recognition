import sys
import cv2
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi


class MainUI(QDialog):
    def __init__(self):
        super(MainUI, self).__init__()
        loadUi("UI.ui", self)
        self.image = None

        self.startButton.clicked.connect(self.start_rec)

    def start_rec(self):
        self.capture = cv2.VideoCapture(0)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.startTimer(5)

    def update_frame(self):
        ret, self.image = self.capture.read()
        self.image = cv2.flip(self.image, 1)
        self.display_image(self.image, 1)

    def display_image(self, img, windows=1):
        qformate = QImage.Format_Indexed8
        if len(img.shape) == 3:
            if img.shape[2] == 4:
                qformate = QImage.Format_RGBA8888
            else:
                qformate = QImage.Format_RGB888

        out = QImage(img, img.shape[1], img.shape[0], img.strides[0], qformate)
        out = out.rgbSwapped()
        if windows == 1:
            self.imgLable.setPixmap(QPixmap.fromImage(out))
            self.imgLable.setScaledContents(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainUI()
    window.setWindowTitle("Amity Security")
    window.show()
    sys.exit(app.exec_())
