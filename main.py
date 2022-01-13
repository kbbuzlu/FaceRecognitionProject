import face_recognition_ui as fr_ui
import sys
from PyQt5 import QtWidgets


class Window(QtWidgets.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()

        self.ui = fr_ui.Ui_MainWindow()
        self.ui.setupUi(self)


def app():
    if not QtWidgets.QApplication.instance():
        app = QtWidgets.QApplication(sys.argv)
    else:
        app = QtWidgets.QApplication.instance()
    window = Window()
    window.show()
    QtWidgets.QApplication.setQuitOnLastWindowClosed(True)
    app.exec_()
    app.quit()


app()
