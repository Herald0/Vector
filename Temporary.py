import pyqtgraph as pg
from PyQt6.QtWidgets import QApplication, QMainWindow
import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from sympy import *
from sympy.plotting import plot, plot3d
# import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Создание графика
        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        # Добавление данных на график
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        y = [30, 32, 34, 32, 33, 31, 29, 32, 35, 45]
        self.graphWidget.plot(x, y)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())

# self.pushButton.clicked.connect(self.fdiff)
#         self.pushButton_2.clicked.connect(self.flim)
#         self.pushButton_3.clicked.connect(self.fdet)
#         self.pushButton_4.clicked.connect(self.frank)
#         self.pushButton_5.clicked.connect(self.IndefInt)
#         self.pushButton_6.clicked.connect(self.DefInt)
#         self.pushButton_7.clicked.connect(self.fplot1)
#         self.pushButton_8.clicked.connect(self.fplot2)
#         self.pushButton_9.clicked.connect(self.fseries)
#         self.pushButton_10.clicked.connect(self.fhelp)
#
#     def fdiff(self):
#             a = self.plainTextEdit.toPlainText().split(',')
#             try:
#                     x = symbols('x')
#                     if len(a) == 1:
#                             res = diff(a[0], x, 1)
#                             self.plainTextEdit_2.setPlainText(str(res))
#                     elif len(a) == 2:
#                             res = diff(a[0], x, a[1])
#                             self.plainTextEdit_2.setPlainText(str(res))
#                     else:
#                             self.plainTextEdit_2.setPlainText("ERROR!")
#             except (ValueError, IndexError, AttributeError, SyntaxError, TypeError):
#                     self.plainTextEdit_2.setPlainText("ERROR!")
#
#     def flim(self):
#             try:
#                     x1 = self.plainTextEdit.toPlainText().lower().split(',')
#                     if len(x1) == 2:
#                             a = x1[0]
#                             n = x1[1]
#                             x = symbols('x')
#                             res = limit(a, x, n)
#                             self.plainTextEdit_2.setPlainText(str(float(res)))
#                     else:
#                             self.plainTextEdit_2.setPlainText("ERROR!")
#             except (ValueError, IndexError, AttributeError, SyntaxError, TypeError):
#                     self.plainTextEdit_2.setPlainText("ERROR!")
#
#     def fdet(self):
#             try:
#                     y = self.plainTextEdit.toPlainText()
#                     a = Matrix(eval(y))
#                     self.plainTextEdit_2.setPlainText(str(a.det()))
#             except (ValueError, IndexError, AttributeError, SyntaxError, TypeError, NameError):
#                     self.plainTextEdit_2.setPlainText("ERROR!")
#
#     def frank(self):
#             try:
#                     y = self.plainTextEdit.toPlainText()
#                     a = Matrix(eval(y))
#                     self.plainTextEdit_2.setPlainText(str(a.rank()))
#             except (ValueError, IndexError, AttributeError, SyntaxError, TypeError, NameError):
#                     self.plainTextEdit_2.setPlainText("ERROR!")
#
#     def IndefInt(self):
#             try:
#                     x1 = self.plainTextEdit.toPlainText().lower()
#                     x = symbols('x')
#                     a = x1
#                     res = integrate(a, x)
#                     self.plainTextEdit_2.setPlainText(str(res))
#             except (ValueError, IndexError, AttributeError, SyntaxError, TypeError):
#                     self.plainTextEdit_2.setPlainText("ERROR!")
#
#     def DefInt(self):
#             try:
#                     y = self.plainTextEdit.toPlainText().lower().split(',')
#                     x = symbols('x')
#                     y1 = eval(y[0])
#                     if len(y) == 3:
#                             res = integrate(y1, (x, y[1], y[2]))
#                             self.plainTextEdit_2.setPlainText(str(float(res)))
#                     else:
#                             self.plainTextEdit_2.setPlainText("ERROR!")
#             except (ValueError, IndexError, AttributeError, SyntaxError, TypeError, NameError):
#                     self.plainTextEdit_2.setPlainText("ERROR!")
#
#     def fplot1(self):
#             try:
#                     y = self.plainTextEdit.toPlainText().lower().split(',')
#                     x = symbols('x')
#                     y1 = eval(y[0])
#                     if len(y) == 1:
#                             plot(y1, (x, -10, 10))
#                             self.plainTextEdit_2.setPlainText("SUCCESS!")
#                     elif len(y) == 3:
#                             plot(y1, (x, y[1], y[2]))
#                             self.plainTextEdit_2.setPlainText("SUCCESS!")
#                     else:
#                             self.plainTextEdit_2.setPlainText("ERROR!")
#             except (ValueError, IndexError, AttributeError, SyntaxError, TypeError, NameError):
#                     self.plainTextEdit_2.setPlainText("ERROR!")
#
#     def fplot2(self):
#             try:
#                     y1 = self.plainTextEdit.toPlainText().lower().split(',')
#                     x, y = symbols('x y')
#                     y2 = eval(y1[0])
#                     if len(y1) == 1:
#                             plot3d(y2, (x, -10, 10), (y, -10, 10))
#                             self.plainTextEdit_2.setPlainText("SUCCESS!")
#                     elif len(y1) == 3:
#                             plot3d(y2, (x, y1[1], y1[2]), (y, y1[1], y1[2]))
#                             self.plainTextEdit_2.setPlainText("SUCCESS!")
#                     else:
#                             self.plainTextEdit_2.setPlainText("ERROR!")
#             except (ValueError, IndexError, AttributeError, SyntaxError, TypeError, NameError):
#                     self.plainTextEdit_2.setPlainText("ERROR!")
#
#     def fseries(self):
#             try:
#                     y = self.plainTextEdit.toPlainText().lower().split(',')
#                     x0 = int(y[1])
#                     e = float(y[2])
#                     if e < 0.0000000001:
#                             e = 0.000000001
#                     n = symbols('n')
#                     a = eval(y[0])
#                     s = a.subs(n, x0)
#                     if len(y) == 3:
#                             for tp in range(x0 + 1, 2000):
#                                     s1 = a.subs(n, tp)
#                                     s += s1
#                                     if abs(s1 - a.subs(n, tp - 1)) < e:
#                                             self.plainTextEdit_2.setPlainText(
#                                                     str(float(s - s1)) + ' | ' + str(tp - 1) + ' steps')
#                                             break
#                     else:
#                             self.plainTextEdit_2.setPlainText("ERROR!")
#             except (ValueError, IndexError, AttributeError, SyntaxError, TypeError, NameError):
#                     self.plainTextEdit_2.setPlainText("ERROR!")
#
#     def fhelp(self):
#             self.plainTextEdit_2.setPlainText("How to use the program:\n"
#     "1)Derivative (function(x), the order of the derivative)\n"
#     "2)Limit (function(x), x->x0(number or 'oo'-infinity))\n"
#     "3)Determinant of the matrix ([[a11,a12,a13...a1n],[a21,a22,a23...a2n]...[am1,am2,am3...amn]])\n"
#     "4)Rank of the matrix ([[a11,a12,a13...a1n],[a21,a22,a23...a2n]...[am1,am2,am3...amn]])\n"
#     "5)Indefinite integral (function(x))\n"
#     "6)Definite integral (function(x), a, b)\n"
#     "7)Plot 2D Graph (function(x), a, b)\n"
#     "8)Plot 3D Graph (function(x), a, b)\n"
#     "9)Sum of the series (sequence(n), n0, precision(epsilon))")
#     def retranslateUi(self, MainWindow):
#             _translate = QtCore.QCoreApplication.translate
#             MainWindow.setWindowTitle(_translate("MainWindow", "Vector"))
#             self.pushButton.setText(_translate("MainWindow", "Derivative"))
#             self.pushButton_2.setText(_translate("MainWindow", "Limit"))
#             self.pushButton_3.setText(_translate("MainWindow", "Determinant of the matrix"))
#             self.pushButton_4.setText(_translate("MainWindow", "The rank of the matrix"))
#             self.pushButton_5.setText(_translate("MainWindow", "Indefinite Integral"))
#             self.pushButton_6.setText(_translate("MainWindow", "Definite Integral"))
#             self.pushButton_7.setText(_translate("MainWindow", "Plot 2D graph"))
#             self.pushButton_8.setText(_translate("MainWindow", "Plot 3D graph"))
#             self.pushButton_9.setText(_translate("MainWindow", "Sum of the series"))
#             self.pushButton_10.setText(_translate("MainWindow", "Help"))
#
#
# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     app.setWindowIcon(QtGui.QIcon('IconCube.png'))
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec())