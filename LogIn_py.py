
from PyQt5 import QtCore, QtGui, QtWidgets
import sys,res_py

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(959, 558)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 30, 550, 500))
        self.widget.setStyleSheet("QPushButton#pushButton, #pushButton_6,#pushButton_8{    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255,255,255,200);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#pushButton:hover, #pushButton_6:hover,#pushButton_8:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#pushButton:pressed, #pushButton_6:pressed,#pushButton_8:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150,123,11,255);\n"
"}\n"
"\n"
"\n"
"QPushButton#pushButton_2{    \n"
"    background-color:rgba(0,0,0,0);\n"
"    color:rgba(85,98,112,255);\n"
"}\n"
"QPushButton#pushButton_2:hover{\n"
"    color:rgba(131,96,53,255);\n"
"}\n"
"QPushButton#pushButton_2:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    color:rgba(91,88,53,255);\n"
"}\n"
"\n"
"\n"
"")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(40, 29, 280, 431))
        self.label.setStyleSheet("background-color:rgba(0,0,0,80);\n"
"border-image: url(:/images/dna_gunu-min.jpg);\n"
"border-top-left-radius: 50px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(260, 29, 240, 431))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-bottom-right-radius: 50px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setGeometry(QtCore.QRect(270, 50, 220, 381))
        self.widget_3.setObjectName("widget_3")
        self.pushButton_6 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_6.setGeometry(QtCore.QRect(15, 260, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit_3.setGeometry(QtCore.QRect(15, 110, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border: none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit_4.setGeometry(QtCore.QRect(15, 60, 85, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border: none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_5 = QtWidgets.QLabel(self.widget_3)
        self.label_5.setGeometry(QtCore.QRect(50, 10, 150, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:rgba(0,0,0,200);")
        self.label_5.setObjectName("label_5")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit_5.setGeometry(QtCore.QRect(120, 60, 85, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border: none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit_6.setGeometry(QtCore.QRect(15, 160, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border: none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.lineEdit_6.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit_7.setGeometry(QtCore.QRect(15, 210, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border: none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.lineEdit_7.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(270, 30, 220, 315))
        self.widget_2.setObjectName("widget_2")
        self.pushButton = QtWidgets.QPushButton(self.widget_2)
        self.pushButton.setGeometry(QtCore.QRect(20, 240, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 160, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border: none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit.setGeometry(QtCore.QRect(20, 95, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border: none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setGeometry(QtCore.QRect(35, 25, 150, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:rgba(0,0,0,200);")
        self.label_3.setObjectName("label_3")
        self.pushButton_8 = QtWidgets.QPushButton(self.widget)
        self.pushButton_8.setGeometry(QtCore.QRect(260, 79, 21, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("border-radius:0px;\n"
"border-top-right-radius:15px;\n"
"bordor-bottom-right-radius:15px;\n"
"\n"
"\n"
"")
        self.pushButton_8.setCheckable(True)
        self.pushButton_8.setObjectName("pushButton_8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 959, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_6.setText(_translate("MainWindow", "R e g i s t e r"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "Email Adress"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "Firs Name"))
        self.label_5.setText(_translate("MainWindow", "Register"))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", "Last Name"))
        self.lineEdit_6.setPlaceholderText(_translate("MainWindow", "Password"))
        self.lineEdit_7.setPlaceholderText(_translate("MainWindow", "Confirm Password"))
        self.pushButton.setText(_translate("MainWindow", "L o g  I n"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Password"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Email"))
        self.label_3.setText(_translate("MainWindow", "LOG IN"))
        self.pushButton_8.setText(_translate("MainWindow", ">"))



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
