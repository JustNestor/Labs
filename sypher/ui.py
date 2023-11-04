# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiLqvLNa.ui'
##
## Created by: Qt User Interface Compiler version 5.15.11
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Form")
        Form.resize(263, 365)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.top = QWidget(Form)
        self.top.setObjectName("top")
        self.verticalLayout_3 = QVBoxLayout(self.top)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.input = QLineEdit(self.top)
        self.input.setObjectName("input")

        self.verticalLayout_3.addWidget(self.input)

        self.spin = QSpinBox(self.top)
        self.spin.setObjectName("spin")

        self.verticalLayout_3.addWidget(self.spin)

        self.check = QRadioButton(self.top)
        self.check.setObjectName("check")

        self.verticalLayout_3.addWidget(self.check)

        self.start = QPushButton(self.top)
        self.start.setObjectName("start")
        self.start.setStyleSheet("")

        self.verticalLayout_3.addWidget(self.start)

        self.verticalLayout.addWidget(self.top)

        self.verticalSpacer = QSpacerItem(
            20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed
        )

        self.verticalLayout.addItem(self.verticalSpacer)

        self.bottom = QWidget(Form)
        self.bottom.setObjectName("bottom")
        self.verticalLayout_2 = QVBoxLayout(self.bottom)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.output = QTextEdit(self.bottom)
        self.output.setObjectName("output")
        self.output.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))
        self.output.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.output)

        self.verticalLayout.addWidget(self.bottom)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(
            QCoreApplication.translate(
                "Form",
                "\u0428\u0438\u0444\u0440 \u0447\u0430\u0441\u0442\u043e\u043a\u043e\u043b\u0443",
                None,
            )
        )
        self.check.setText(
            QCoreApplication.translate(
                "Form",
                "\u0420\u043e\u0437\u0448\u0438\u0444\u0440\u0443\u0432\u0430\u0442\u0438",
                None,
            )
        )
        self.start.setText(
            QCoreApplication.translate(
                "Form", "\u0417\u0430\u043f\u0443\u0441\u043a", None
            )
        )

    # retranslateUi
