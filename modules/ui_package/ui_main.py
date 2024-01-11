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
    QSizePolicy, QTabWidget, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(905, 699)
        MainWindow.setContextMenuPolicy(Qt.DefaultContextMenu)
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.header = QFrame(self.centralwidget)
        self.header.setObjectName(u"header")
        self.header.setMinimumSize(QSize(891, 121))
        self.header.setMaximumSize(QSize(891, 121))
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.header)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_9 = QFrame(self.header)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"border: 1px solid rgba(0, 0, 0, .3);\n"
"border-radius: 5%;\n"
"\n"
"background: qlineargradient(spread:reflect, x1:0.506, y1:0, x2:0.488636, y2:1, stop:0 rgba(0, 0, 22, 10), stop:1 rgba(0, 0, 86, 10));\n"
"border-top: 2px solid rgba(0, 0, 0, .3);")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.frame_9.setLineWidth(1)
        self.verticalLayout_15 = QVBoxLayout(self.frame_9)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_21 = QLabel(self.frame_9)
        self.label_21.setObjectName(u"label_21")
        font = QFont()
        font.setBold(True)
        self.label_21.setFont(font)
        self.label_21.setMouseTracking(False)
        self.label_21.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.label_21.setLayoutDirection(Qt.LeftToRight)
        self.label_21.setStyleSheet(u"border: 0;\n"
"border-radius: 0%;")
        self.label_21.setScaledContents(True)
        self.label_21.setAlignment(Qt.AlignCenter)
        self.label_21.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextEditable)

        self.verticalLayout_15.addWidget(self.label_21)

        self.label_22 = QLabel(self.frame_9)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMouseTracking(False)
        self.label_22.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.label_22.setLayoutDirection(Qt.LeftToRight)
        self.label_22.setStyleSheet(u"border: 0;\n"
"border-radius: 0%;")
        self.label_22.setScaledContents(True)
        self.label_22.setAlignment(Qt.AlignCenter)
        self.label_22.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextEditable)

        self.verticalLayout_15.addWidget(self.label_22)


        self.verticalLayout.addWidget(self.frame_9)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_3 = QFrame(self.header)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"border: 1px solid rgba(0, 0, 0, .3);\n"
"border-radius: 5%;\n"
"\n"
"background: qlineargradient(spread:reflect, x1:0.506, y1:0, x2:0.488636, y2:1, stop:0 rgba(0, 0, 22, 10), stop:1 rgba(0, 0, 86, 10));")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_3.setLineWidth(1)
        self.verticalLayout_7 = QVBoxLayout(self.frame_3)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setMouseTracking(False)
        self.label_5.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.label_5.setLayoutDirection(Qt.LeftToRight)
        self.label_5.setStyleSheet(u"border: 0;\n"
"border-radius: 0%;")
        self.label_5.setScaledContents(True)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_5.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextEditable)

        self.verticalLayout_7.addWidget(self.label_5)

        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMouseTracking(False)
        self.label_6.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.label_6.setLayoutDirection(Qt.LeftToRight)
        self.label_6.setStyleSheet(u"border: 0;\n"
"border-radius: 0%;")
        self.label_6.setScaledContents(True)
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_6.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextEditable)

        self.verticalLayout_7.addWidget(self.label_6)


        self.horizontalLayout.addWidget(self.frame_3)

        self.frame_7 = QFrame(self.header)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"border: 1px solid rgba(0, 0, 0, .3);\n"
"border-radius: 2%;\n"
"\n"
"background: qlineargradient(spread:reflect, x1:0.506, y1:0, x2:0.488636, y2:1, stop:0 rgba(0, 0, 22, 10), stop:1 rgba(0, 0, 86, 10));")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.frame_7.setLineWidth(1)
        self.verticalLayout_13 = QVBoxLayout(self.frame_7)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_17 = QLabel(self.frame_7)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font)
        self.label_17.setMouseTracking(False)
        self.label_17.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.label_17.setLayoutDirection(Qt.LeftToRight)
        self.label_17.setStyleSheet(u"border: 0;\n"
"border-radius: 0%;")
        self.label_17.setScaledContents(True)
        self.label_17.setAlignment(Qt.AlignCenter)
        self.label_17.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextEditable)

        self.verticalLayout_13.addWidget(self.label_17)

        self.label_18 = QLabel(self.frame_7)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMouseTracking(False)
        self.label_18.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.label_18.setLayoutDirection(Qt.LeftToRight)
        self.label_18.setStyleSheet(u"border: 0;\n"
"border-radius: 0%;")
        self.label_18.setScaledContents(True)
        self.label_18.setAlignment(Qt.AlignCenter)
        self.label_18.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextEditable)

        self.verticalLayout_13.addWidget(self.label_18)


        self.horizontalLayout.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.header)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"border: 1px solid rgba(0, 0, 0, .3);\n"
"border-radius: 5%;\n"
"\n"
"background: qlineargradient(spread:reflect, x1:0.506, y1:0, x2:0.488636, y2:1, stop:0 rgba(0, 0, 22, 10), stop:1 rgba(0, 0, 86, 10));")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.frame_8.setLineWidth(1)
        self.verticalLayout_14 = QVBoxLayout(self.frame_8)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_19 = QLabel(self.frame_8)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font)
        self.label_19.setMouseTracking(False)
        self.label_19.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.label_19.setLayoutDirection(Qt.LeftToRight)
        self.label_19.setStyleSheet(u"border: 0;\n"
"border-radius: 0%;")
        self.label_19.setScaledContents(True)
        self.label_19.setAlignment(Qt.AlignCenter)
        self.label_19.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextEditable)

        self.verticalLayout_14.addWidget(self.label_19)

        self.label_20 = QLabel(self.frame_8)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMouseTracking(False)
        self.label_20.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.label_20.setLayoutDirection(Qt.LeftToRight)
        self.label_20.setStyleSheet(u"border: 0;\n"
"border-radius: 0%;")
        self.label_20.setScaledContents(True)
        self.label_20.setAlignment(Qt.AlignCenter)
        self.label_20.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextEditable)

        self.verticalLayout_14.addWidget(self.label_20)


        self.horizontalLayout.addWidget(self.frame_8)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_3.addWidget(self.header)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"")
        self.widget1 = QWidget(self.widget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(10, 10, 873, 509))
        self.verticalLayout_4 = QVBoxLayout(self.widget1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.textEdit = QTextEdit(self.widget1)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(871, 51))
        self.textEdit.setMaximumSize(QSize(871, 51))
        font1 = QFont()
        font1.setBold(False)
        self.textEdit.setFont(font1)
        self.textEdit.setMouseTracking(False)
        self.textEdit.setStyleSheet(u"background-color: transparent;")
        self.textEdit.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout_4.addWidget(self.textEdit)

        self.answer_GroupBox = QGroupBox(self.widget1)
        self.answer_GroupBox.setObjectName(u"answer_GroupBox")
        self.answer_GroupBox.setMinimumSize(QSize(871, 401))
        self.answer_GroupBox.setMaximumSize(QSize(871, 401))
        self.verticalLayout_5 = QVBoxLayout(self.answer_GroupBox)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")

        self.verticalLayout_4.addWidget(self.answer_GroupBox)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_2 = QFrame(self.widget1)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(201, 41))
        self.frame_2.setMaximumSize(QSize(201, 16777215))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.btn_end = QPushButton(self.frame_2)
        self.btn_end.setObjectName(u"btn_end")

        self.horizontalLayout_5.addWidget(self.btn_end)


        self.horizontalLayout_3.addWidget(self.frame_2)

        self.frame_5 = QFrame(self.widget1)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(451, 41))
        self.frame_5.setMaximumSize(QSize(451, 41))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.line = QFrame(self.frame_5)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_6.addWidget(self.line)

        self.btn_save = QPushButton(self.frame_5)
        self.btn_save.setObjectName(u"btn_save")

        self.horizontalLayout_6.addWidget(self.btn_save)

        self.line_2 = QFrame(self.frame_5)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_6.addWidget(self.line_2)


        self.horizontalLayout_3.addWidget(self.frame_5)

        self.frame_4 = QFrame(self.widget1)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(201, 41))
        self.frame_4.setMaximumSize(QSize(201, 41))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.btn_back = QPushButton(self.frame_4)
        self.btn_back.setObjectName(u"btn_back")

        self.horizontalLayout_4.addWidget(self.btn_back)

        self.btn_next = QPushButton(self.frame_4)
        self.btn_next.setObjectName(u"btn_next")

        self.horizontalLayout_4.addWidget(self.btn_next)


        self.horizontalLayout_3.addWidget(self.frame_4)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)


        self.verticalLayout_3.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 905, 19))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u0441\u0442", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u0441\u0442 \u043d\u0430 \u043e\u0431\u0449\u0435\u0435 \u0440\u0430\u0437\u0432\u0438\u0442\u0438\u0435", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u0441\u0442\u0438\u0440\u0443\u0435\u043c\u044b\u0439", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u043b\u0438\u0442\u0432\u0438\u043d \u0414\u0430\u043d\u0438\u043b\u0430 \u0421\u0435\u0440\u0433\u0435\u0435\u0432\u0438\u0447", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0441\u0442\u0430\u043b\u043e\u0441\u044c \u0432\u0440\u0435\u043c\u0435\u043d\u0438", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0441\u0442\u0430\u043b\u043e\u0441\u044c \u0432\u043e\u043f\u0440\u043e\u0441\u043e\u0432", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"13", None))
        self.textEdit.setMarkdown(QCoreApplication.translate("MainWindow", u"fdsfsd\n"
"\n"
"", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Tahoma'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:5px; margin-bottom:5px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">fdsfsd</p></body></html>", None))
        self.btn_end.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0432\u0435\u0440\u0448\u0438\u0442\u044c \u0442\u0435\u0441\u0442", None))
        self.btn_save.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043e\u0442\u0432\u0435\u0442", None))
        self.btn_back.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.btn_next.setText(QCoreApplication.translate("MainWindow", u">", None))
    # retranslateUi

