# from numpy import *
# import matplotlib.pyplot as plt
#
# x = linspace(0, 2, 100)
# plt.plot(x, 3*x, 'r')
# x = linspace(2, 3, 100)
# plt.plot(x, x*0, 'r')
#
# x = linspace(0, 3, 100)
# plt.plot(x, 8/6+x*0)
# x = linspace(0, 3, 100)
# k = 4
# S1 = 8/6 + (-9/pi*sqrt(3)/2 - 27/(8*pi**2)-27/(4*pi**2))*cos(2*pi*x/3) + (3/(2*pi)-27/(4*pi**2)*sqrt(3)/2)*sin(2*pi*x/3)
# S2 = S1 + (9/(2*pi)*sqrt(3)/2 - 27/(32*pi**2)-27/(16*pi**2))*cos(4*pi*x/3) + (3/(4*pi)+27/(16*pi**2)*sqrt(3)/2)*sin(4*pi*x/3)
# S3 = S2 + (3/(4*pi**2)-3/(4*pi**2))*cos(2*pi*x)-1/pi*sin(2*pi*x)
# S4 = S3 + (9/(k*pi)*sin(4*pi*k/3) + 27/(4*pi**2*k**2)-27/(4*pi**2*k**2))*cos(2*k*pi*x/3) + (-3/(k*pi)*cos(4*pi*k/3)+27/(4*pi**2*k**2)*sin(4*pi*k/3))*sin(2*k*pi*x/3)
# plt.plot(x, S1)
# plt.plot(x, S2)
# plt.plot(x, S3)
# plt.plot(x, S4, 'm')
# plt.grid(True)
# plt.show()
from PyQt6 import QtCore, QtGui, QtWidgets
from sympy import *
from sympy.plotting import plot, plot3d
import pyqtgraph as pg
import numpy as np
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1216, 700)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(193, 24, 124, 1), stop:0.427447 rgba(120, 0, 180, 130), stop:1 rgba(170, 86, 229, 0.33));\n"
"font-family: Bahnschrift;")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(14, 0, 1192, 659))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(parent=self.widget)
        self.plainTextEdit.setStyleSheet("QPlainTextEdit {\n"
"font-size: 45px;\n"
"border: 2px solid black;\n"
"border-radius: 10px;\n"
"}")
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout.addWidget(self.plainTextEdit)
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(parent=self.widget)
        self.plainTextEdit_2.setEnabled(False)
        self.plainTextEdit_2.setStyleSheet("QPlainTextEdit {\n"
"color: black;\n"
"font-size: 35px;\n"
"border: 2px solid black;\n"
"border-radius: 10px;\n"
"}")
        self.plainTextEdit_2.setPlainText("")
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.verticalLayout.addWidget(self.plainTextEdit_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.graphicsView = pg.PlotWidget(parent=self.widget)
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayout.addWidget(self.graphicsView)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(parent=self.widget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"color: white;\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 120px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70)\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton_2.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"color: white;\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 120px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70)\n"
"}\n"
"color: white;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.widget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"color: white;\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 120px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70)\n"
"}\n"
"color: white;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.widget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"color: white;\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 120px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70)\n"
"}\n"
"color: white;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_9 = QtWidgets.QPushButton(parent=self.widget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("QPushButton {\n"
"color: white;\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 120px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"border: 2px solid black;\n"
"}\n"
"color: white;")
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_2.addWidget(self.pushButton_9)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.widget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton {\n"
"color: white;\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 120px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70)\n"
"}\n"
"color: white;")
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_3.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.widget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("QPushButton {\n"
"color: white;\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 120px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70)\n"
"}\n"
"color: white;")
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_3.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(parent=self.widget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("QPushButton {\n"
"color: white;\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 120px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70)\n"
"}\n"
"color: white;")
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_3.addWidget(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(parent=self.widget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("QPushButton {\n"
"color: white;\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 120px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70)\n"
"}\n"
"color: white;")
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_3.addWidget(self.pushButton_8)
        self.pushButton_10 = QtWidgets.QPushButton(parent=self.widget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("QPushButton {\n"
"color: white;\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 120px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"border: 2px solid black;\n"
"}\n"
"color: white;")
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout_3.addWidget(self.pushButton_10)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.fdiff)
        self.pushButton_2.clicked.connect(self.flim)
        self.pushButton_3.clicked.connect(self.fdet)
        self.pushButton_4.clicked.connect(self.frank)
        self.pushButton_5.clicked.connect(self.IndefInt)
        self.pushButton_6.clicked.connect(self.DefInt)
        self.pushButton_7.clicked.connect(self.fplot1)
        self.pushButton_8.clicked.connect(self.fplot2)
        self.pushButton_9.clicked.connect(self.fseries)
        self.pushButton_10.clicked.connect(self.fhelp)

    def fdiff(self):
            a = self.plainTextEdit.toPlainText().split(',')
            try:
                    x = symbols('x')
                    if len(a) == 1:
                            res = diff(a[0], x, 1)
                            self.plainTextEdit_2.setPlainText(str(res))
                    elif len(a) == 2:
                            res = diff(a[0], x, a[1])
                            self.plainTextEdit_2.setPlainText(str(res))
                    else:
                            self.plainTextEdit_2.setPlainText("ERROR!")
            except (ValueError, IndexError, AttributeError, SyntaxError, TypeError):
                    self.plainTextEdit_2.setPlainText("ERROR!")

    def flim(self):
            try:
                    x1 = self.plainTextEdit.toPlainText().lower().split(',')
                    if len(x1) == 2:
                            a = x1[0]
                            n = x1[1]
                            x = symbols('x')
                            res = limit(a, x, n)
                            self.plainTextEdit_2.setPlainText(str(float(res)))
                    else:
                            self.plainTextEdit_2.setPlainText("ERROR!")
            except (ValueError, IndexError, AttributeError, SyntaxError, TypeError):
                    self.plainTextEdit_2.setPlainText("ERROR!")

    def fdet(self):
            try:
                    y = self.plainTextEdit.toPlainText()
                    a = Matrix(eval(y))
                    self.plainTextEdit_2.setPlainText(str(a.det()))
            except (ValueError, IndexError, AttributeError, SyntaxError, TypeError, NameError):
                    self.plainTextEdit_2.setPlainText("ERROR!")

    def frank(self):
            try:
                    y = self.plainTextEdit.toPlainText()
                    a = Matrix(eval(y))
                    self.plainTextEdit_2.setPlainText(str(a.rank()))
            except (ValueError, IndexError, AttributeError, SyntaxError, TypeError, NameError):
                    self.plainTextEdit_2.setPlainText("ERROR!")

    def IndefInt(self):
            try:
                    x1 = self.plainTextEdit.toPlainText().lower()
                    x = symbols('x')
                    a = x1
                    res = integrate(a, x)
                    self.plainTextEdit_2.setPlainText(str(res))
            except (ValueError, IndexError, AttributeError, SyntaxError, TypeError):
                    self.plainTextEdit_2.setPlainText("ERROR!")

    def DefInt(self):
            try:
                    y = self.plainTextEdit.toPlainText().lower().split(',')
                    x = symbols('x')
                    y1 = eval(y[0])
                    if len(y) == 3:
                            res = integrate(y1, (x, y[1], y[2]))
                            self.plainTextEdit_2.setPlainText(str(float(res)))
                    else:
                            self.plainTextEdit_2.setPlainText("ERROR!")
            except (ValueError, IndexError, AttributeError, SyntaxError, TypeError, NameError):
                    self.plainTextEdit_2.setPlainText("ERROR!")

    def fplot1(self):
            try:
                    y = self.plainTextEdit.toPlainText().lower().split(',')
                    x = symbols('x')
                    y1 = eval(y[0])
                    if len(y) ==1:
                            x1 = list(np.linspace(-10, 10, 21))
                            y2 = [y1.subs(x, a) for a in x1]
                            print('1:', x1)
                            print('2:', y2)
                            print(len(x1)==len(y2))
                            self.graphicsView.plot(list(x1), list(y2))
                            self.plainTextEdit_2.setPlainText("SUCCESS!")
                    elif len(y) == 3:
                            self.graphWidget = pg.PlotWidget()
                            w = self.graphWidget.setCentralWidget(self.graphWidget)
                            print(1)
                            # Добавление данных на график
                            x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                            y = [30, 32, 34, 32, 33, 31, 29, 32, 35, 45]
                            self.graphicsView.plot(x, y)
                            # plot(y1, (x, -10, 10))
                            self.plainTextEdit_2.setPlainText("SUCCESS!")
                    else:
                            self.plainTextEdit_2.setPlainText("ERROR444!")
            except (ValueError, IndexError, AttributeError, SyntaxError, TypeError, NameError):
                    self.plainTextEdit_2.setPlainText("ERROR!")

    def fplot2(self):
            try:
                    y1 = self.plainTextEdit.toPlainText().lower().split(',')
                    x, y = symbols('x y')
                    y2 = eval(y1[0])
                    if len(y1) == 1:
                            plot3d(y2, (x, -10, 10), (y, -10, 10))
                            self.plainTextEdit_2.setPlainText("SUCCESS!")
                    elif len(y1) == 3:
                            plot3d(y2, (x, y1[1], y1[2]), (y, y1[1], y1[2]))
                            self.plainTextEdit_2.setPlainText("SUCCESS!")
                    else:
                            self.plainTextEdit_2.setPlainText("ERROR!")
            except (ValueError, IndexError, AttributeError, SyntaxError, TypeError, NameError):
                    self.plainTextEdit_2.setPlainText("ERROR!")

    def fseries(self):
            try:
                    y = self.plainTextEdit.toPlainText().lower().split(',')
                    x0 = int(y[1])
                    e = float(y[2])
                    if e < 0.0000000001:
                            e = 0.000000001
                    n = symbols('n')
                    a = eval(y[0])
                    s = a.subs(n, x0)
                    if len(y) == 3:
                            for tp in range(x0 + 1, 2000):
                                    s1 = a.subs(n, tp)
                                    s += s1
                                    if abs(s1 - a.subs(n, tp - 1)) < e:
                                            self.plainTextEdit_2.setPlainText(
                                                    str(float(s - s1)) + ' | ' + str(tp - 1) + ' steps')
                                            break
                    else:
                            self.plainTextEdit_2.setPlainText("ERROR!")
            except (ValueError, IndexError, AttributeError, SyntaxError, TypeError, NameError):
                    self.plainTextEdit_2.setPlainText("ERROR!")

    def fhelp(self):
            self.plainTextEdit_2.setPlainText("How to use the program:\n"
    "1)Derivative (function(x), the order of the derivative)\n"
    "2)Limit (function(x), x->x0(number or 'oo'-infinity))\n"
    "3)Determinant of the matrix ([[a11,a12,a13...a1n],[a21,a22,a23...a2n]...[am1,am2,am3...amn]])\n"
    "4)Rank of the matrix ([[a11,a12,a13...a1n],[a21,a22,a23...a2n]...[am1,am2,am3...amn]])\n"
    "5)Indefinite integral (function(x))\n"
    "6)Definite integral (function(x), a, b)\n"
    "7)Plot 2D Graph (function(x), a, b)\n"
    "8)Plot 3D Graph (function(x), a, b)\n"
    "9)Sum of the series (sequence(n), n0, precision(epsilon))")
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Vector"))
        self.pushButton.setText(_translate("MainWindow", "Derivative"))
        self.pushButton_2.setText(_translate("MainWindow", "Limit"))
        self.pushButton_3.setText(_translate("MainWindow", "Determinant of the matrix"))
        self.pushButton_4.setText(_translate("MainWindow", "The rank of the matrix"))
        self.pushButton_9.setText(_translate("MainWindow", "Sum of the series"))
        self.pushButton_5.setText(_translate("MainWindow", "Indefinite Integral"))
        self.pushButton_6.setText(_translate("MainWindow", "Definite Integral"))
        self.pushButton_7.setText(_translate("MainWindow", "Building 2D grapht"))
        self.pushButton_8.setText(_translate("MainWindow", "Building 3D graph"))
        self.pushButton_10.setText(_translate("MainWindow", "Sum of the series"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
