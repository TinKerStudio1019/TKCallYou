# Form implementation generated from reading ui file 'd:\PythonProject\CallYou!\UI_SeniorEditor.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_SeniorEditor(object):
    def setupUi(self, SeniorEditor):
        SeniorEditor.setObjectName("SeniorEditor")
        SeniorEditor.resize(271, 189)
        SeniorEditor.setMinimumSize(QtCore.QSize(271, 189))
        font = QtGui.QFont()
        font.setFamily("阿里巴巴普惠体 3.0 55 Regular")
        SeniorEditor.setFont(font)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(SeniorEditor)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = QtWidgets.QWidget(parent=SeniorEditor)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.titleLabel = QtWidgets.QLabel(parent=self.widget)
        font = QtGui.QFont()
        font.setFamily("阿里巴巴普惠体 3.0 95 ExtraBold")
        font.setPointSize(18)
        font.setBold(True)
        self.titleLabel.setFont(font)
        self.titleLabel.setObjectName("titleLabel")
        self.verticalLayout.addWidget(self.titleLabel)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.option1CheckBox = CheckBox(parent=self.widget)
        self.option1CheckBox.setObjectName("option1CheckBox")
        self.horizontalLayout.addWidget(self.option1CheckBox)
        self.option1WenHao = TransparentPushButton(parent=self.widget)
        self.option1WenHao.setObjectName("option1WenHao")
        self.horizontalLayout.addWidget(self.option1WenHao)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.option2CheckBox = CheckBox(parent=self.widget)
        self.option2CheckBox.setObjectName("option2CheckBox")
        self.horizontalLayout.addWidget(self.option2CheckBox)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.plainTextEdit = PlainTextEdit(parent=self.widget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout.addWidget(self.plainTextEdit)
        self.sendPbtn = PushButton(parent=self.widget)
        self.sendPbtn.setObjectName("sendPbtn")
        self.verticalLayout.addWidget(self.sendPbtn)
        self.verticalLayout_2.addWidget(self.widget)

        self.retranslateUi(SeniorEditor)
        QtCore.QMetaObject.connectSlotsByName(SeniorEditor)

    def retranslateUi(self, SeniorEditor):
        _translate = QtCore.QCoreApplication.translate
        SeniorEditor.setWindowTitle(_translate("SeniorEditor", "Form"))
        self.titleLabel.setText(_translate("SeniorEditor", "高级编辑器"))
        self.option1CheckBox.setText(_translate("SeniorEditor", "要求接收端确定收到"))
        self.option1WenHao.setText(_translate("SeniorEditor", "？"))
        self.option2CheckBox.setText(_translate("SeniorEditor", "启用语音"))
        self.sendPbtn.setText(_translate("SeniorEditor", "发射！"))
from qfluentwidgets import CheckBox, PlainTextEdit, PushButton, TransparentPushButton