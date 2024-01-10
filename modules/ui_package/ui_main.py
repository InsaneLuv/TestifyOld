# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QHBoxLayout,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox_question = QGroupBox(self.centralwidget)
        self.groupBox_question.setObjectName(u"groupBox_question")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_question)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.question_text = QLabel(self.groupBox_question)
        self.question_text.setObjectName(u"question_text")

        self.verticalLayout_2.addWidget(self.question_text)

        self.question_separator = QFrame(self.groupBox_question)
        self.question_separator.setObjectName(u"question_separator")
        self.question_separator.setFrameShape(QFrame.HLine)
        self.question_separator.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.question_separator)

        self.question_description = QLabel(self.groupBox_question)
        self.question_description.setObjectName(u"question_description")

        self.verticalLayout_2.addWidget(self.question_description)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addWidget(self.groupBox_question)

        self.groupBox_answer = QGroupBox(self.centralwidget)
        self.groupBox_answer.setObjectName(u"groupBox_answer")
        self.verticalLayout = QVBoxLayout(self.groupBox_answer)
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.verticalLayout_3.addWidget(self.groupBox_answer)

        self.groupBox_buttons = QGroupBox(self.centralwidget)
        self.groupBox_buttons.setObjectName(u"groupBox_buttons")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_buttons)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.button_back = QPushButton(self.groupBox_buttons)
        self.button_back.setObjectName(u"button_back")

        self.horizontalLayout.addWidget(self.button_back)

        self.button_sub = QPushButton(self.groupBox_buttons)
        self.button_sub.setObjectName(u"button_sub")

        self.horizontalLayout.addWidget(self.button_sub)

        self.button_next = QPushButton(self.groupBox_buttons)
        self.button_next.setObjectName(u"button_next")

        self.horizontalLayout.addWidget(self.button_next)


        self.verticalLayout_5.addLayout(self.horizontalLayout)


        self.verticalLayout_3.addWidget(self.groupBox_buttons)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 19))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox_question.setTitle(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 \u043d\u043e\u043c\u0435\u0440", None))
        self.question_text.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 TEXT", None))
        self.question_description.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 DESC", None))
        self.groupBox_answer.setTitle(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0432\u0435\u0442\u044b", None))
        self.groupBox_buttons.setTitle(QCoreApplication.translate("MainWindow", u"\u041a\u043d\u043e\u043f\u043a\u0438", None))
        self.button_back.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.button_sub.setText(QCoreApplication.translate("MainWindow", u"Sub", None))
        self.button_next.setText(QCoreApplication.translate("MainWindow", u"Next", None))
    # retranslateUi

