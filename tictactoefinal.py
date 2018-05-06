# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tictactoefinal.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Tic-Tac-Toe")
        MainWindow.resize(666, 599)

        self.chance = 'X'
        self.turn = 0
        self.mw = MainWindow

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(210, 110, 111, 111))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(36)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setAutoFillBackground(False)
        self.pushButton_1.setText("")
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 110, 111, 111))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(36)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(430, 110, 111, 111))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(36)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(210, 220, 111, 111))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(36)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(320, 220, 111, 111))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(36)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(430, 220, 111, 111))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(36)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setText("")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(210, 330, 111, 111))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(36)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setText("")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(320, 330, 111, 111))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(36)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setText("")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(430, 330, 111, 111))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(36)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setText("")
        self.pushButton_9.setObjectName("pushButton_9")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(210, 500, 331, 41))
        font = QtGui.QFont()
        font.setFamily("Typewriter")
        font.setPointSize(16)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(310, 460, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Symbola")
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 40, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Dyuthi")
        font.setPointSize(52)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 666, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.pushButton_1.clicked.connect(self.changebtn1)
        self.pushButton_2.clicked.connect(self.changebtn2)
        self.pushButton_3.clicked.connect(self.changebtn3)
        self.pushButton_4.clicked.connect(self.changebtn4)
        self.pushButton_5.clicked.connect(self.changebtn5)
        self.pushButton_6.clicked.connect(self.changebtn6)
        self.pushButton_7.clicked.connect(self.changebtn7)
        self.pushButton_8.clicked.connect(self.changebtn8)
        self.pushButton_9.clicked.connect(self.changebtn9)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Tic-Tac-Toe"))
        self.label.setText(_translate("MainWindow", "Result"))
        self.combination = [[self.pushButton_1, self.pushButton_2, self.pushButton_3],
                            [self.pushButton_4, self.pushButton_5, self.pushButton_6],
                            [self.pushButton_7, self.pushButton_8, self.pushButton_9],
                            [self.pushButton_1, self.pushButton_4, self.pushButton_7],
                            [self.pushButton_2, self.pushButton_5, self.pushButton_8],
                            [self.pushButton_3, self.pushButton_6, self.pushButton_9],
                            [self.pushButton_1, self.pushButton_5, self.pushButton_9],
                            [self.pushButton_3, self.pushButton_5, self.pushButton_7]]

    def changebtn1(self):
        text = self.changeValue(self.pushButton_1)

    def changebtn2(self):
        text = self.changeValue(self.pushButton_2)

    def changebtn3(self):
        text = self.changeValue(self.pushButton_3)

    def changebtn4(self):
        text = self.changeValue(self.pushButton_4)

    def changebtn5(self):
        text = self.changeValue(self.pushButton_5)

    def changebtn6(self):
        text = self.changeValue(self.pushButton_6)

    def changebtn7(self):
        text = self.changeValue(self.pushButton_7)

    def changebtn8(self):
        text = self.changeValue(self.pushButton_8)

    def changebtn9(self):
        text = self.changeValue(self.pushButton_9)

    def reset(self):
        self.turn.set(0)

    def changeValue(self, btn):

        text = btn.text()

        if "X" in text or "O" in text:
            pass
        else:
            btn.setText(self.chance)
            if "X" in self.chance:
                self.chance = "O"
            else:
                self.chance = "X"
        self.turn += 1
        if self.turn > 4:
            check = self.checker(btn)
            is_winner = self.checker(btn)
            if is_winner:
                if 'O' in self.chance:

                    self.textEdit.setText("X won")
                    return

                else:
                    self.textEdit.setText("O won")

                    return

        if self.turn == 9:
            self.textEdit.setText("Draw")
            return

    def checker(self, btn):
        value = btn.text()
        for row in self.combination:
            if btn in row:
                flag = True
                for item in row:
                    if value == item.text():
                        continue
                    else:
                        flag = False
                        break
                if flag:
                    return True
        return False

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())