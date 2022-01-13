# -*- coding: utf-8 -*-
#
# Created by: PyQt5 UI code generator 5.9.2
#

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QImage
import cv2, imutils
import ImageAnalyze, faces



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1500, 1000)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("color: rgb(51, 51, 51);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet("background-color: rgb(153, 153, 153);")
        self.centralwidget.setObjectName("centralwidget")
        self.imgLabel = QtWidgets.QLabel(self.centralwidget)
        self.imgLabel.setGeometry(QtCore.QRect(10, 10, 1200, 900))
        self.imgLabel.setText("")
        self.imgLabel.setObjectName("imgLabel")
        self.btn_fotograf = QtWidgets.QPushButton(self.centralwidget)
        self.btn_fotograf.setGeometry(QtCore.QRect(1330, 140, 140, 31))
        self.btn_fotograf.setStyleSheet("background-color: rgb(223, 175, 198);\n"
"font-weight: bold;\n"
"")
        self.btn_fotograf.setObjectName("btn_fotograf")
        self.btn_fotograf.clicked.connect(self.load_image)
        self.btn_kameraAc = QtWidgets.QPushButton(self.centralwidget)
        self.btn_kameraAc.setGeometry(QtCore.QRect(1330, 220, 140, 31))
        self.btn_kameraAc.setStyleSheet("background-color: rgb(223, 175, 198);\n"
"font-weight: bold;\n"
"")
        self.btn_kameraAc.setObjectName("btn_kameraAc")
        self.btn_kameraAc.clicked.connect(self.live_face)
        self.btn_yuzTanima = QtWidgets.QPushButton(self.centralwidget)
        self.btn_yuzTanima.setGeometry(QtCore.QRect(1330, 300, 140, 31))
        self.btn_yuzTanima.setStyleSheet("background-color: rgb(223, 175, 198);\n"
"font-weight: bold;\n"
"")
        self.btn_yuzTanima.setObjectName("btn_yuzTanima")
        self.btn_yuzTanima.clicked.connect(self.face_recognize)
        self.btn_yasCinsiyet = QtWidgets.QPushButton(self.centralwidget)
        self.btn_yasCinsiyet.setGeometry(QtCore.QRect(1330, 380, 140, 31))
        self.btn_yasCinsiyet.setStyleSheet("background-color: rgb(223, 175, 198);\n"
"font-weight: bold;\n"
"")
        self.btn_yasCinsiyet.setObjectName("btn_yasCinsiyet")
        self.btn_yasCinsiyet.clicked.connect(self.get_age_gender_race)
        self.btn_duyguTahmin = QtWidgets.QPushButton(self.centralwidget)
        self.btn_duyguTahmin.setGeometry(QtCore.QRect(1330, 460, 140, 31))
        self.btn_duyguTahmin.setStyleSheet("background-color: rgb(223, 175, 198);\n"
"font-weight: bold;\n"
"")
        self.btn_duyguTahmin.setObjectName("btn_close")
        self.btn_duyguTahmin.clicked.connect(self.get_emotion)

        self.btn_close= QtWidgets.QPushButton(self.centralwidget)
        self.btn_close.setGeometry(QtCore.QRect(1330, 540, 140, 31))
        self.btn_close.setStyleSheet("background-color: rgb(223, 175, 198);\n"
"font-weight: bold;\n"
"")
        self.btn_close.setObjectName("btn_close")
        self.btn_close.clicked.connect(self.close)


        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.filename = None
        self.temp = None
        self.analyze = None


    def load_image(self):
        self.filename = QFileDialog.getOpenFileName(filter="Image (*.*)")[0]
        self.image = cv2.imread(self.filename)
        self.set_photo(self.image)

    def set_photo(self, image):
        self.temp = image
        image = imutils.resize(image, width=1200, height=1200)
        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
        self.imgLabel.setPixmap(QtGui.QPixmap.fromImage(image))

    def get_age_gender_race(self):
        self.analyze = ImageAnalyze.image_analyze(self.image)
        img = ImageAnalyze.age_gender_race_analyze(self.image,self.analyze)
        self.set_photo(img)

    def face_recognize(self):
        img = faces.face_recognition_func(self.image)
        self.set_photo(img)

    def get_emotion(self):
        self.analyze = ImageAnalyze.image_analyze(self.image)
        img = ImageAnalyze.emotion_analyze(self.image, self.analyze)
        self.set_photo(img)

    def live_face(self):
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            faces.face_recognition_func(frame)
            #cv2.imshow("frame", frame)
            self.set_photo(frame)

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
        #cap.release()
        #cv2.destroyAllWindows()

    def close(self):
        self.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Face Recognition"))
        self.btn_fotograf.setText(_translate("MainWindow", "Fotoğraf Yükle"))
        self.btn_kameraAc.setText(_translate("MainWindow", "Kamera Aç"))
        self.btn_yuzTanima.setText(_translate("MainWindow", "Yüz Tanıma"))
        self.btn_yasCinsiyet.setText(_translate("MainWindow", "Yaş-Cinsiyet Tahmini"))
        self.btn_duyguTahmin.setText(_translate("MainWindow", "Duygu Tahmini"))
        self.btn_close.setText(_translate("MainWindow", "Çıkış"))
