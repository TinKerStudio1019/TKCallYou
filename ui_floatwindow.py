# Form implementation generated from reading ui file 'd:\PythonProject\CallYou!\UI_FloatWindow.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_FloatWindow(object):
    def setupUi(self, FloatWindow):
        FloatWindow.setObjectName("FloatWindow")
        FloatWindow.resize(1920, 300)
        FloatWindow.setMinimumSize(QtCore.QSize(1920, 150))
        FloatWindow.setMaximumSize(QtCore.QSize(1920, 300))
        self.verticalLayout = QtWidgets.QVBoxLayout(FloatWindow)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(parent=FloatWindow)
        self.widget.setStyleSheet(".QWidget {background-color: rgba(0, 0, 0, 160);\n"
"color: rgba(255, 255, 255, 220);}")
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.TextLabel = QtWidgets.QLabel(parent=self.widget)
        font = QtGui.QFont()
        font.setFamily("阿里巴巴普惠体 3.0 75 SemiBold")
        font.setPointSize(64)
        font.setBold(True)
        self.TextLabel.setFont(font)
        self.TextLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.TextLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.TextLabel.setWordWrap(True)
        self.TextLabel.setObjectName("TextLabel")
        self.verticalLayout_2.addWidget(self.TextLabel)
        self.RestTimeProgressBar = QtWidgets.QProgressBar(parent=self.widget)
        self.RestTimeProgressBar.setMaximumSize(QtCore.QSize(16777215, 10))
        self.RestTimeProgressBar.setStyleSheet("QProgressBar {background-color: rgba(0, 0, 0, 0);}\n"
"QProgressBar::chunk {background-color: rgb(55, 205, 84)}")
        self.RestTimeProgressBar.setMaximum(100000)
        self.RestTimeProgressBar.setProperty("value", 100000)
        self.RestTimeProgressBar.setTextVisible(False)
        self.RestTimeProgressBar.setTextDirection(QtWidgets.QProgressBar.Direction.TopToBottom)
        self.RestTimeProgressBar.setObjectName("RestTimeProgressBar")
        self.verticalLayout_2.addWidget(self.RestTimeProgressBar)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(FloatWindow)
        QtCore.QMetaObject.connectSlotsByName(FloatWindow)

    def retranslateUi(self, FloatWindow):
        _translate = QtCore.QCoreApplication.translate
        FloatWindow.setWindowTitle(_translate("FloatWindow", "Form"))
        self.TextLabel.setText(_translate("FloatWindow", "TextLabel"))