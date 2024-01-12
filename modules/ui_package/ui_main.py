# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'good.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QTextBrowser,
    QVBoxLayout, QWidget)
from .res_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(919, 665)
        MainWindow.setStyleSheet(u"")
        self.main = QWidget(MainWindow)
        self.main.setObjectName(u"main")
        self.main.setStyleSheet(u"QPushButton {\n"
"background-color:rgba(0, 0, 0,10);\n"
"border: 1px solid black;\n"
"border-radius: 5px;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:rgba(0, 0, 0,20);\n"
"border: 1px solid black;\n"
"border-radius: 5px;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color:rgba(0, 0, 0,10);\n"
"border: 1px solid black;\n"
"border-radius: 5px;\n"
"font-weight: bold;\n"
"}	\n"
"\n"
"\n"
"QLineEdit {\n"
"background-color:rgba(0, 0, 0,10);\n"
"border-radius: 5px;\n"
"padding: 5px;\n"
"}\n"
"QCheckBox {\n"
"background-color:rgba(0, 0, 0,10);\n"
"border-radius: 5px;\n"
"padding: 5px;\n"
"}\n"
"QRadioButton {\n"
"background-color:rgba(0, 0, 0,10);\n"
"border-radius: 5px;\n"
"padding: 5px;\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    background-color:rgba(0, 0, 0,20);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"background-color:rgba(0, 0, 0,10);\n"
"border-radius: 2px;\n"
"border: 1px solid black;\n"
"}\n"
"\n"
"QRadioButton::"
                        "indicator::unchecked {\n"
"background-color:rgba(0, 0, 0,10);\n"
"border-radius: 5px;\n"
"border: 1px solid black;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:hover {\n"
"    background-color:rgba(0, 0, 0,20);\n"
"}\n"
"\n"
"QFrame#answer {\n"
"background-color:rgba(0, 0, 0,10);\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////// */\n"
"\n"
"QTextBrowser#question_text {\n"
"background-color:rgba(0, 0, 0,10);\n"
"border-radius: 5px;\n"
"padding: 5px;\n"
"}\n"
"\n"
"QTextBrowser#question_text:hover {\n"
"background-color:rgba(0, 0, 0,15);\n"
"}\n"
"\n"
"QFrame#question {\n"
"background-color:rgba(0, 0, 0,10);\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QFrame#buttons {\n"
"background-color:rgba(0, 0, 0,10);\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QWidget#main {\n"
"background-color:rgba(0, 0, 0,30);\n"
"}\n"
"QFrame#headerTitle {\n"
"background-color:rgba(0, 0, 0,10);\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QFrame#cats {\n"
"background-color:rgba(0, 0, 0,10);\n"
"b"
                        "order-radius: 5px;\n"
"}\n"
"\n"
"QFrame#cat_user {\n"
"background-color:rgba(0, 0, 0,10);\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QFrame#cat_timer {\n"
"background-color:rgba(0, 0, 0,10);\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QFrame#cat_remain {\n"
"background-color:rgba(0, 0, 0,10);\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QFrame#cat_user:hover {\n"
"background-color:rgba(0, 0, 0,15);\n"
"}\n"
"\n"
"QFrame#cat_timer:hover {\n"
"background-color:rgba(0, 0, 0,15);\n"
"}\n"
"\n"
"QFrame#cat_remain:hover {\n"
"background-color:rgba(0, 0, 0,15);\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.main)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.headerTitle = QFrame(self.main)
        self.headerTitle.setObjectName(u"headerTitle")
        self.headerTitle.setMaximumSize(QSize(901, 58))
        self.headerTitle.setFrameShape(QFrame.StyledPanel)
        self.headerTitle.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.headerTitle)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.container_header = QFrame(self.headerTitle)
        self.container_header.setObjectName(u"container_header")
        self.container_header.setFrameShape(QFrame.StyledPanel)
        self.container_header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.container_header)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.container_icon = QFrame(self.container_header)
        self.container_icon.setObjectName(u"container_icon")
        self.container_icon.setMaximumSize(QSize(33, 49))
        self.container_icon.setFrameShape(QFrame.StyledPanel)
        self.container_icon.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.container_icon)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 0, 5, 0)
        self.icon_dataset = QLabel(self.container_icon)
        self.icon_dataset.setObjectName(u"icon_dataset")
        self.icon_dataset.setMinimumSize(QSize(21, 21))
        self.icon_dataset.setMaximumSize(QSize(21, 21))
        self.icon_dataset.setLayoutDirection(Qt.LeftToRight)
        self.icon_dataset.setPixmap(QPixmap(u":/icons/icons/grid.svg"))
        self.icon_dataset.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.icon_dataset)


        self.horizontalLayout_2.addWidget(self.container_icon)

        self.container_content = QFrame(self.container_header)
        self.container_content.setObjectName(u"container_content")
        self.container_content.setStyleSheet(u"QLabel#label_cur {\n"
"font-weight: bold;\n"
"}")
        self.container_content.setFrameShape(QFrame.StyledPanel)
        self.container_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.container_content)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, -1, 7)
        self.label_cur = QLabel(self.container_content)
        self.label_cur.setObjectName(u"label_cur")
        font = QFont()
        font.setBold(True)
        self.label_cur.setFont(font)

        self.verticalLayout.addWidget(self.label_cur)

        self.label_title = QLabel(self.container_content)
        self.label_title.setObjectName(u"label_title")
        font1 = QFont()
        font1.setItalic(False)
        font1.setUnderline(False)
        self.label_title.setFont(font1)

        self.verticalLayout.addWidget(self.label_title)


        self.horizontalLayout_2.addWidget(self.container_content)


        self.horizontalLayout_3.addWidget(self.container_header)


        self.verticalLayout_2.addWidget(self.headerTitle)

        self.cats = QFrame(self.main)
        self.cats.setObjectName(u"cats")
        self.cats.setMinimumSize(QSize(901, 91))
        self.cats.setMaximumSize(QSize(901, 91))
        self.cats.setFrameShape(QFrame.StyledPanel)
        self.cats.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.cats)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.cat_user = QFrame(self.cats)
        self.cat_user.setObjectName(u"cat_user")
        self.cat_user.setMinimumSize(QSize(290, 73))
        self.cat_user.setMaximumSize(QSize(290, 73))
        self.cat_user.setFrameShape(QFrame.StyledPanel)
        self.cat_user.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.cat_user)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.container_icon_catname = QFrame(self.cat_user)
        self.container_icon_catname.setObjectName(u"container_icon_catname")
        self.container_icon_catname.setStyleSheet(u"font-weight: bold;")
        self.container_icon_catname.setFrameShape(QFrame.StyledPanel)
        self.container_icon_catname.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.container_icon_catname)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.container_icon_catname)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 5, 0, 0)
        self.icon_2 = QLabel(self.frame)
        self.icon_2.setObjectName(u"icon_2")
        self.icon_2.setMinimumSize(QSize(21, 21))
        self.icon_2.setMaximumSize(QSize(21, 21))
        self.icon_2.setLayoutDirection(Qt.LeftToRight)
        self.icon_2.setStyleSheet(u"")
        self.icon_2.setPixmap(QPixmap(u":/icons/icons/person.svg"))
        self.icon_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.icon_2)


        self.verticalLayout_5.addWidget(self.frame)

        self.frame_2 = QFrame(self.container_icon_catname)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_cur_2 = QLabel(self.frame_2)
        self.label_cur_2.setObjectName(u"label_cur_2")
        self.label_cur_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_cur_2)


        self.verticalLayout_5.addWidget(self.frame_2)


        self.verticalLayout_3.addWidget(self.container_icon_catname)

        self.container_content_2 = QFrame(self.cat_user)
        self.container_content_2.setObjectName(u"container_content_2")
        self.container_content_2.setFrameShape(QFrame.StyledPanel)
        self.container_content_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.container_content_2)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 9)
        self.label_user = QLabel(self.container_content_2)
        self.label_user.setObjectName(u"label_user")
        self.label_user.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.horizontalLayout_6.addWidget(self.label_user)


        self.verticalLayout_3.addWidget(self.container_content_2)


        self.horizontalLayout_12.addWidget(self.cat_user)

        self.cat_timer = QFrame(self.cats)
        self.cat_timer.setObjectName(u"cat_timer")
        self.cat_timer.setFrameShape(QFrame.StyledPanel)
        self.cat_timer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.cat_timer)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.container_icon_catname_2 = QFrame(self.cat_timer)
        self.container_icon_catname_2.setObjectName(u"container_icon_catname_2")
        self.container_icon_catname_2.setStyleSheet(u"font-weight: bold;")
        self.container_icon_catname_2.setFrameShape(QFrame.StyledPanel)
        self.container_icon_catname_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.container_icon_catname_2)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.container_icon_catname_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 5, 0, 0)
        self.icon = QLabel(self.frame_7)
        self.icon.setObjectName(u"icon")
        self.icon.setMinimumSize(QSize(21, 21))
        self.icon.setMaximumSize(QSize(21, 21))
        self.icon.setLayoutDirection(Qt.LeftToRight)
        self.icon.setPixmap(QPixmap(u":/icons/icons/timer.svg"))
        self.icon.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.icon)


        self.verticalLayout_7.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.container_icon_catname_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_8)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_cur_3 = QLabel(self.frame_8)
        self.label_cur_3.setObjectName(u"label_cur_3")
        self.label_cur_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_cur_3)


        self.verticalLayout_7.addWidget(self.frame_8)


        self.verticalLayout_6.addWidget(self.container_icon_catname_2)

        self.container_content_3 = QFrame(self.cat_timer)
        self.container_content_3.setObjectName(u"container_content_3")
        self.container_content_3.setFrameShape(QFrame.StyledPanel)
        self.container_content_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.container_content_3)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 9)
        self.label_timer = QLabel(self.container_content_3)
        self.label_timer.setObjectName(u"label_timer")
        self.label_timer.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.horizontalLayout_7.addWidget(self.label_timer)


        self.verticalLayout_6.addWidget(self.container_content_3)


        self.horizontalLayout_12.addWidget(self.cat_timer)

        self.cat_remain = QFrame(self.cats)
        self.cat_remain.setObjectName(u"cat_remain")
        self.cat_remain.setFrameShape(QFrame.StyledPanel)
        self.cat_remain.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.cat_remain)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.container_icon_catname_3 = QFrame(self.cat_remain)
        self.container_icon_catname_3.setObjectName(u"container_icon_catname_3")
        self.container_icon_catname_3.setStyleSheet(u"font-weight: bold;")
        self.container_icon_catname_3.setFrameShape(QFrame.StyledPanel)
        self.container_icon_catname_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.container_icon_catname_3)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.container_icon_catname_3)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 5, 0, 0)
        self.icon_3 = QLabel(self.frame_10)
        self.icon_3.setObjectName(u"icon_3")
        self.icon_3.setMinimumSize(QSize(21, 21))
        self.icon_3.setMaximumSize(QSize(21, 21))
        self.icon_3.setLayoutDirection(Qt.LeftToRight)
        self.icon_3.setPixmap(QPixmap(u":/icons/icons/lists.svg"))
        self.icon_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.icon_3)


        self.verticalLayout_10.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.container_icon_catname_3)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_11)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_cur_4 = QLabel(self.frame_11)
        self.label_cur_4.setObjectName(u"label_cur_4")
        self.label_cur_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_cur_4)


        self.verticalLayout_10.addWidget(self.frame_11)


        self.verticalLayout_9.addWidget(self.container_icon_catname_3)

        self.container_content_4 = QFrame(self.cat_remain)
        self.container_content_4.setObjectName(u"container_content_4")
        self.container_content_4.setFrameShape(QFrame.StyledPanel)
        self.container_content_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.container_content_4)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 9)
        self.label_remain = QLabel(self.container_content_4)
        self.label_remain.setObjectName(u"label_remain")
        self.label_remain.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.horizontalLayout_8.addWidget(self.label_remain)


        self.verticalLayout_9.addWidget(self.container_content_4)


        self.horizontalLayout_12.addWidget(self.cat_remain)


        self.verticalLayout_2.addWidget(self.cats)

        self.question = QFrame(self.main)
        self.question.setObjectName(u"question")
        self.question.setMaximumSize(QSize(901, 142))
        self.question.setFrameShape(QFrame.StyledPanel)
        self.question.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.question)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.container_question = QFrame(self.question)
        self.container_question.setObjectName(u"container_question")
        self.container_question.setMaximumSize(QSize(901, 142))
        self.container_question.setFrameShape(QFrame.StyledPanel)
        self.container_question.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.container_question)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.container_content_5 = QFrame(self.container_question)
        self.container_content_5.setObjectName(u"container_content_5")
        self.container_content_5.setMinimumSize(QSize(899, 140))
        self.container_content_5.setStyleSheet(u"QLabel#label_cur {\n"
"font-weight: bold;\n"
"}")
        self.container_content_5.setFrameShape(QFrame.StyledPanel)
        self.container_content_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.container_content_5)
        self.verticalLayout_12.setSpacing(9)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(9, 9, 9, 9)
        self.frame_3 = QFrame(self.container_content_5)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(879, 30))
        self.frame_3.setMaximumSize(QSize(879, 30))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_16.setSpacing(5)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.icon_4 = QLabel(self.frame_3)
        self.icon_4.setObjectName(u"icon_4")
        self.icon_4.setMinimumSize(QSize(21, 21))
        self.icon_4.setMaximumSize(QSize(21, 21))
        self.icon_4.setLayoutDirection(Qt.LeftToRight)
        self.icon_4.setPixmap(QPixmap(u":/icons/icons/quiz.svg"))
        self.icon_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.icon_4)

        self.label_question_num = QLabel(self.frame_3)
        self.label_question_num.setObjectName(u"label_question_num")
        self.label_question_num.setFont(font)
        self.label_question_num.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_16.addWidget(self.label_question_num)


        self.verticalLayout_12.addWidget(self.frame_3)

        self.container_content_7 = QFrame(self.container_content_5)
        self.container_content_7.setObjectName(u"container_content_7")
        self.container_content_7.setFrameShape(QFrame.StyledPanel)
        self.container_content_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.container_content_7)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.question_text = QTextBrowser(self.container_content_7)
        self.question_text.setObjectName(u"question_text")
        self.question_text.setMinimumSize(QSize(0, 79))
        self.question_text.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.question_text.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.question_text.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout_13.addWidget(self.question_text)


        self.verticalLayout_12.addWidget(self.container_content_7)


        self.horizontalLayout_14.addWidget(self.container_content_5)


        self.horizontalLayout_13.addWidget(self.container_question)


        self.verticalLayout_2.addWidget(self.question)

        self.answer = QFrame(self.main)
        self.answer.setObjectName(u"answer")
        self.answer.setMinimumSize(QSize(901, 271))
        self.answer.setMaximumSize(QSize(901, 16777215))
        self.answer.setFrameShape(QFrame.StyledPanel)
        self.answer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.answer)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")

        self.verticalLayout_2.addWidget(self.answer)

        self.buttons = QFrame(self.main)
        self.buttons.setObjectName(u"buttons")
        self.buttons.setMinimumSize(QSize(901, 61))
        self.buttons.setMaximumSize(QSize(901, 61))
        self.buttons.setFrameShape(QFrame.StyledPanel)
        self.buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.buttons)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.container_buttons = QFrame(self.buttons)
        self.container_buttons.setObjectName(u"container_buttons")
        self.container_buttons.setFrameShape(QFrame.StyledPanel)
        self.container_buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.container_buttons)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(50, 0, 50, 0)
        self.btn_end = QPushButton(self.container_buttons)
        self.btn_end.setObjectName(u"btn_end")
        self.btn_end.setMinimumSize(QSize(161, 31))
        self.btn_end.setMaximumSize(QSize(161, 31))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/exit.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_end.setIcon(icon1)
        self.btn_end.setIconSize(QSize(24, 24))
        self.btn_end.setAutoRepeat(False)

        self.horizontalLayout_15.addWidget(self.btn_end)


        self.horizontalLayout_4.addWidget(self.container_buttons)

        self.container_buttons_2 = QFrame(self.buttons)
        self.container_buttons_2.setObjectName(u"container_buttons_2")
        self.container_buttons_2.setFrameShape(QFrame.StyledPanel)
        self.container_buttons_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.container_buttons_2)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(50, 0, 50, 0)
        self.btn_save = QPushButton(self.container_buttons_2)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setMinimumSize(QSize(161, 31))
        self.btn_save.setMaximumSize(QSize(161, 31))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/check.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_save.setIcon(icon2)
        self.btn_save.setIconSize(QSize(24, 24))
        self.btn_save.setAutoRepeat(False)

        self.horizontalLayout_17.addWidget(self.btn_save)


        self.horizontalLayout_4.addWidget(self.container_buttons_2)

        self.container_buttons_3 = QFrame(self.buttons)
        self.container_buttons_3.setObjectName(u"container_buttons_3")
        self.container_buttons_3.setFrameShape(QFrame.StyledPanel)
        self.container_buttons_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.container_buttons_3)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.container_nav_buttons = QFrame(self.container_buttons_3)
        self.container_nav_buttons.setObjectName(u"container_nav_buttons")
        self.container_nav_buttons.setMinimumSize(QSize(211, 51))
        self.container_nav_buttons.setMaximumSize(QSize(211, 51))
        self.container_nav_buttons.setFrameShape(QFrame.StyledPanel)
        self.container_nav_buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.container_nav_buttons)
        self.horizontalLayout_5.setSpacing(9)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(9, 0, 9, 9)
        self.btn_prev = QPushButton(self.container_nav_buttons)
        self.btn_prev.setObjectName(u"btn_prev")
        self.btn_prev.setMinimumSize(QSize(91, 31))
        self.btn_prev.setMaximumSize(QSize(91, 31))
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/prev.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_prev.setIcon(icon3)
        self.btn_prev.setIconSize(QSize(24, 24))
        self.btn_prev.setAutoRepeat(False)

        self.horizontalLayout_5.addWidget(self.btn_prev)

        self.btn_next = QPushButton(self.container_nav_buttons)
        self.btn_next.setObjectName(u"btn_next")
        self.btn_next.setMinimumSize(QSize(91, 31))
        self.btn_next.setMaximumSize(QSize(91, 31))
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/next.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_next.setIcon(icon4)
        self.btn_next.setIconSize(QSize(24, 24))
        self.btn_next.setAutoRepeat(False)

        self.horizontalLayout_5.addWidget(self.btn_next)


        self.horizontalLayout_18.addWidget(self.container_nav_buttons)


        self.horizontalLayout_4.addWidget(self.container_buttons_3)


        self.verticalLayout_2.addWidget(self.buttons)

        MainWindow.setCentralWidget(self.main)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("")
        self.icon_dataset.setText("")
        self.label_cur.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u0441\u0442", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"PLACEHOLDER", None))
        self.icon_2.setText("")
        self.label_cur_2.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u0441\u0442\u0438\u0440\u0443\u0435\u043c\u044b\u0439", None))
        self.label_user.setText(QCoreApplication.translate("MainWindow", u"PLACEHOLDER", None))
        self.icon.setText("")
        self.label_cur_3.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0441\u0442\u0430\u043b\u043e\u0441\u044c \u0432\u0440\u0435\u043c\u0435\u043d\u0438", None))
        self.label_timer.setText(QCoreApplication.translate("MainWindow", u"PLACEHOLDER", None))
        self.icon_3.setText("")
        self.label_cur_4.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0441\u0442\u0430\u043b\u043e\u0441\u044c \u0432\u043e\u043f\u0440\u043e\u0441\u043e\u0432", None))
        self.label_remain.setText(QCoreApplication.translate("MainWindow", u"PLACEHOLDER", None))
        self.icon_4.setText("")
        self.label_question_num.setText(QCoreApplication.translate("MainWindow", u"PLACEHOLDER", None))
        self.question_text.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">PLACEHOLDER</p></body></html>", None))
        self.btn_end.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0432\u0435\u0440\u0448\u0438\u0442\u044c \u0442\u0435\u0441\u0442", None))
#if QT_CONFIG(shortcut)
        self.btn_end.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.btn_save.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043e\u0442\u0432\u0435\u0442", None))
#if QT_CONFIG(shortcut)
        self.btn_save.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.btn_prev.setText("")
#if QT_CONFIG(shortcut)
        self.btn_prev.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.btn_next.setText("")
#if QT_CONFIG(shortcut)
        self.btn_next.setShortcut("")
#endif // QT_CONFIG(shortcut)
    # retranslateUi

