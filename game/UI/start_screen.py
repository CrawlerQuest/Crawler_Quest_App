from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1003, 540)
        self.formLayout = QtWidgets.QFormLayout(Form)
        self.formLayout.setObjectName("formLayout")
        self.title_card = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.title_card.setFont(font)
        self.title_card.setScaledContents(True)
        self.title_card.setObjectName("title_card")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.title_card)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.quit_game_button = QtWidgets.QPushButton(Form)
        self.quit_game_button.setObjectName("quit_game_button")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.quit_game_button)
        self.start_game_button = QtWidgets.QPushButton(Form)
        self.start_game_button.setObjectName("start_game_button")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.start_game_button)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.title_card.setText(_translate("Form", "Crawler Quest"))
        self.quit_game_button.setText(_translate("Form", "Quit Game"))
        self.start_game_button.setText(_translate("Form", "Start Game"))
