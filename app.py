from typing import Optional
from PySide6.QtCore import Qt, QStringListModel
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget,QListView
import sys
from modules import Ui_MainWindow
from modules import Question
import random

class Tester(QMainWindow):
    def __init__(self, question_list):
        super(Tester, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.question_list = question_list
        self.ui.button_next.clicked.connect(self._next)
        self.ui.button_back.clicked.connect(self._back)
        self.ui.button_sub.clicked.connect(self._sub)
        self.current_question_index = 0
        self.set_question(question_list[self.current_question_index])

    def clear_question(self):
        layout = self.ui.groupBox_answer.layout()
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
            else:
                spacer = item.spacerItem()
                if spacer:
                    layout.removeItem(spacer)

    def set_question(self, question):
        self.clear_question()
        self.ui.question_text.setText(question.qu_title)
        self.ui.question_description.setText(question.qu_description)
        self.list_view = QListView()
        self.list_model = QStringListModel()

        self.list = question.qu_variants
        self.list_model.setStringList(self.list)
        self.list_view.setModel(self.list_model)
        self.ui.groupBox_answer.layout().addWidget(self.list_view)

    def _next(self):
        self.set_question(self.question_list[1])

    def _back(self):
        self.set_question(self.question_list[0])

    def _sub(self):
        pass




if __name__ == '__main__':
    questions = [Question(
        title='Вопрос текст',
        description='Дескриптион',
        mode='choose_one',
        variants=['var1','var2','var3'],
        answer='var1'
    ),Question(
        title='Вопрос2 текст',
        description='Дескриптион3',
        mode='choose_one',
        variants=['var33','var44','var55'],
        answer='var55'
    )]
    app = QApplication(sys.argv)
    window = Tester(questions)
    window.show()
    sys.exit(app.exec())