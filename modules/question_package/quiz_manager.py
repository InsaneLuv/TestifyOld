from .grade import Grade
class QuizManager:
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

    def count_grade(self):
        grade = Grade(self.questions)
        print(grade.correct, grade.uncorrect)