from typing import Optional
from PySide6.QtCore import QTimer, QTime, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QCheckBox, QLineEdit, QRadioButton, QTextBrowser, QPushButton
import sys
from modules import Question, QuestionModes, Ui_MainWindow, QuizManager, TimerManager


class QuizWindow(QMainWindow):
    def __init__(self, questions, total_time_minutes, winTitle, quizTitle, userName):
        super(QuizWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle(f"Testify | {winTitle}")
        self.quizTitle = quizTitle
        self.userName = userName
        self.QuizManager = QuizManager(questions)
        self.timer_manager = TimerManager(total_time_minutes, self.update_timer_label)
        self.ended = False
        self.on_startup()

    def on_startup(self):
        self.QuizManager.select_question()
        self.__setup_header()
        self.__setup_question()
        self.__setup_btn_callbacks()

    def __setup_header(self):
        self.ui.label_22.setText(self.quizTitle)
        self.ui.label_6.setText(self.userName)
        self.timer_manager.start_timer()

    def __setup_question(self):
        self.ui.textEdit.setText(self.QuizManager.selected_question.title)
        self.set_remain()
        self.setup_answer_widget()
    
    def __setup_btn_callbacks(self):
        self.ui.btn_end.clicked.connect(self.handle_btn_end)
        self.ui.btn_save.clicked.connect(self.handle_btn_save)
        self.ui.btn_back.clicked.connect(self.handle_btn_back)
        self.ui.btn_next.clicked.connect(self.handle_btn_next)

    def update_timer_label(self, remaining_time):
        self.ui.label_18.setText(remaining_time.toString("hh:mm:ss"))
        if remaining_time == QTime(0, 0):
            self.ended = True
            self.ended_event()

    def ended_event(self):
        self.disable_buttons()
        self.timer_manager.stop_timer()

    def disable_buttons(self):
        self.ui.btn_back.setEnabled(False)
        self.ui.btn_next.setEnabled(False)
    
    def set_remain(self):
        remain = len(self.QuizManager.get_unsubmitted())
        self.ui.label_20.setText(str(remain))
        if remain == 1:
            self.ended = True
            self.ended_event()

    def handle_btn_end(self):
        self.clear_layout(self.ui.answer_GroupBox.layout())
        self.QuizManager.count_grade()

    def handle_btn_save(self):
        self.QuizManager.selected_question.submitted = True
        self.QuizManager.selected_question.user_answer = self.QuizManager.selected_question.temp_user_answer_selected
        if not self.ended:
            self.handle_btn_next()
        else:
            self.ui.btn_save.setEnabled(False)
            self.set_remain()
            self.ui.answer_GroupBox.setEnabled(False)

    def handle_btn_back(self):
        self.QuizManager.scroll_question('prev')
        self.__setup_question()

    def handle_btn_next(self):
        self.QuizManager.scroll_question('next')
        self.__setup_question()

    def setup_answer_widget(self):
        self.clear_layout(self.ui.answer_GroupBox.layout())
        
        self.answer_widgets = []

        question = self.QuizManager.selected_question

        if question.mode == QuestionModes.INPUT:
            input_lineedit = QLineEdit(self)
            input_lineedit.setPlaceholderText("Введите ответ")
            input_lineedit.textChanged.connect(self.handle_answer_changed)
            self.ui.answer_GroupBox.layout().addWidget(input_lineedit)
            self.answer_widgets.append(input_lineedit)

        if question.mode == QuestionModes.CHOOSE_ONE:
            for variant in question.variants:
                radio_button = QRadioButton(variant, self)
                radio_button.clicked.connect(self.handle_answer_changed)
                self.ui.answer_GroupBox.layout().addWidget(radio_button)
                self.answer_widgets.append(radio_button)

        if question.mode == QuestionModes.CHOOSE:
            for variant in question.variants:
                checkbox = QCheckBox(variant, self)
                checkbox.clicked.connect(self.handle_answer_changed)
                self.ui.answer_GroupBox.layout().addWidget(checkbox)
                self.answer_widgets.append(checkbox)
                
        self.keep_choosen()

    def keep_choosen(self):
        question = self.QuizManager.selected_question
        if question.temp_user_answer_selected:
            if question.mode == QuestionModes.INPUT:
                self.answer_widgets[0].setText(question.temp_user_answer_selected)

            if question.mode == QuestionModes.CHOOSE_ONE:
                for widget in self.answer_widgets:
                    if widget.text() == question.temp_user_answer_selected:
                        widget.setChecked(True)

            if question.mode == QuestionModes.CHOOSE:
                for widget in self.answer_widgets:
                    if widget.text() in question.temp_user_answer_selected:
                        widget.setChecked(True)

    def handle_answer_changed(self):
        question = self.QuizManager.selected_question

        if question.mode == QuestionModes.INPUT:
            question.set_temp_user_answer_selected(self.answer_widgets[0].text())

        elif question.mode == QuestionModes.CHOOSE_ONE:
            for widget in self.answer_widgets:
                if widget.isChecked():
                    question.set_temp_user_answer_selected(widget.text())

        elif question.mode == QuestionModes.CHOOSE:
            user_answer = []
            for widget in self.answer_widgets:
                if widget.isChecked():
                    user_answer.append(widget.text())
            question.set_temp_user_answer_selected(user_answer)

    def clear_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
            else:
                spacer = item.spacerItem()
                if spacer:
                    layout.removeItem(spacer)


if __name__ == '__main__':
    questions = [Question(
        title='Sample Choose Question',
        description='This is a sample choose question.',
        mode=QuestionModes.CHOOSE,
        variants=['Option A', 'Option B', 'Option C', 'Option D'],
        correct_answer=['Option A', 'Option C']
    ), Question(
        title='Sample Choose Question2',
        description='This is a sample choose question.',
        mode=QuestionModes.CHOOSE_ONE,
        variants=['Option A', 'Option B', 'Option C', 'Option D'],
        correct_answer='Option A'
    ),
    Question(
        title='Sample Choose Question3',
        description='This is a sample choose question.',
        mode=QuestionModes.INPUT,
        correct_answer='Option A'
    )]
    app = QApplication(sys.argv)
    window = QuizWindow(questions, total_time_minutes=1, winTitle = 'Тест', quizTitle='Тест обычный', userName='Данила')
    window.show()
    sys.exit(app.exec())