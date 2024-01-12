class Grade:
    def __init__(self, questions) -> None:
        self.questions = questions
        self.correct = 0
        self.uncorrect = 0
        self.total = len(questions)
        self.count()
    
    def count(self):
        for question in self.questions:
            if question.check_answer():
                self.correct += 1
            else:
                self.uncorrect += 1
            question.submitted = True