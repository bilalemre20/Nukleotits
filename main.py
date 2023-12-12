from PyQt5 import QtWidgets, QtCore
from LogIn_py import Ui_MainWindow
import sys


class LoginApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def changeform(self):
        if self.ui.pushButton_8.isChecked():
            self.ui.widget_2.hide()
            self.ui.widget_3.show()
        else:
            self.ui.widget_2.show()
            self.ui.widget_3.hide()

    def __init__(self):
        super(LoginApp, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.ui.label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.ui.label_3.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.ui.pushButton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))
        self.ui.pushButton_6.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))

        self.ui.widget_3.hide()

        self.ui.pushButton_8.clicked.connect(self.changeform)
        self.center()
    def center(self):
        frame_geometry = self.frameGeometry()
        desktop_center = QtWidgets.QDesktopWidget().availableGeometry().center()
        frame_geometry.moveCenter(desktop_center)
        self.move(frame_geometry.topLeft())

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = LoginApp()
    MainWindow.show()
    sys.exit(app.exec_())
