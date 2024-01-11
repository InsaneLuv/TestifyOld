from typing import Optional
from PySide6.QtCore import QTimer, QTime, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QCheckBox, QLineEdit, QRadioButton, QTextBrowser, QPushButton
import sys
from modules import Ui_MainWindow
from modules import Question, QuestionModes

class QuizManager():
    def __init__(self, questions):
        self.questions = questions
        self.selected_question = None
        self.selected_question_index = 0
    
    def select_question(self):
        for index, question in enumerate(self.questions):
            if not question.submitted:
                self.selected_question = question
                self.selected_question_index = index
                return question

    def scroll_question(self, mode):
        direction = 1 if mode == 'next' else -1
        original_index = self.selected_question_index
        while True:
            self.selected_question_index = (self.selected_question_index + direction) % len(self.questions)
            if self.selected_question_index == original_index:
                break
            if not self.questions[self.selected_question_index].submitted:
                self.selected_question = self.questions[self.selected_question_index]
                return self.selected_question

    
    def get_unsubmitted(self):
        return [question for question in self.questions if not question.submitted]


        

class TimerManager:
    def __init__(self, total_time_minutes, update_callback):
        self.total_time_seconds = total_time_minutes * 60
        self.elapsed_time_seconds = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)
        self.update_callback = update_callback

    def start_timer(self):
        self.timer.start(1000)

    def stop_timer(self):
        self.timer.stop()

    def update_timer(self):
        self.elapsed_time_seconds += 1
        remaining_time = self.calculate_remaining_time()
        self.update_callback(remaining_time)

        if remaining_time == QTime(0, 0):
            self.timer.stop()

    def calculate_remaining_time(self):
        remaining_time_seconds = max(0, self.total_time_seconds - self.elapsed_time_seconds)
        remaining_time = QTime(0, 0).addSecs(remaining_time_seconds)
        return remaining_time

class QuizWindow(QMainWindow):
    def __init__(self, questions, total_time_minutes):
        super(QuizWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.QuizManager = QuizManager(questions)
        self.timer_manager = TimerManager(total_time_minutes, self.update_timer_label)
        self.ended = False
        self.on_startup()

    def on_startup(self):
        self.QuizManager.select_question()
        self.setup_question()
        self.timer_manager.start_timer()
        self.__setup_btn_callbacks()

    def update_timer_label(self, remaining_time):
        self.ui.label_18.setText(remaining_time.toString("hh:mm:ss"))
        if remaining_time == QTime(0, 0):
            self.ended = True
            self.disable_buttons()

    def disable_buttons(self):
        self.ui.btn_back.setEnabled(False)
        self.ui.btn_next.setEnabled(False)

    def setup_question(self):
        self.ui.textEdit.setText(self.QuizManager.selected_question.title)
        self.set_remain()
        self.setup_answer_widget()
    
    def set_remain(self):
        self.ui.label_20.setText(str(len(self.QuizManager.get_unsubmitted())))

    def __setup_btn_callbacks(self):
        # self.ui.btn_end.clicked.connect(self.handle_btn_end)
        self.ui.btn_save.clicked.connect(self.handle_btn_save)
        self.ui.btn_back.clicked.connect(self.handle_btn_back)
        self.ui.btn_next.clicked.connect(self.handle_btn_next)

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
        self.setup_question()

    def handle_btn_next(self):
        self.QuizManager.scroll_question('next')
        self.setup_question()

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
    window = QuizWindow(questions, 0.05)
    window.show()
    sys.exit(app.exec())