from enum import Enum
import inspect

class QuestionModes(Enum):
    CHOOSE = 'choose'
    CHOOSE_ONE = 'choose_one'
    INPUT = 'input'

class Question:
    def __init__(self, title, description=None, mode=None, variants=None, correct_answer=None, threshold_similarity=0.4, threshold_length_diff=2):
        self.title = title
        self.description = description
        self.mode = mode
        self.variants = variants
        self.correct_answer = correct_answer

        self.threshold_similarity = threshold_similarity
        self.threshold_length_diff = threshold_length_diff

        self.temp_user_answer_selected = None

        self.user_answer = None

        self.submitted = False
        self.validate_question()

    def set_temp_user_answer_selected(self, selected):
        caller_frame = inspect.currentframe().f_back
        caller_func_name = caller_frame.f_code.co_name
        print(f'Caller {caller_func_name} = {selected}')
        self.temp_user_answer_selected = selected

    def check_answer(self):
        if not self.user_answer:
            raise ValueError(f"No user_answer set")
        if self.mode == QuestionModes.INPUT:
            return self.user_answer.lower() == self.correct_answer.lower()

        elif self.mode == QuestionModes.CHOOSE_ONE:
            return self.user_answer in self.correct_answer

        elif self.mode == QuestionModes.CHOOSE:
            return self.user_answer == self.correct_answer

    def validate_question(self):
        if self.mode not in QuestionModes:
            raise ValueError(f"Unknown question mode: {self.mode}")

        if self.mode == QuestionModes.INPUT:
            if self.variants is not None:
                raise ValueError("Variants should be None for 'input' mode.")

        elif self.mode == QuestionModes.CHOOSE_ONE:
            if self.variants is None or not self.variants or self.correct_answer not in self.variants or not isinstance(self.correct_answer, str):
                raise ValueError("Invalid configuration for 'choose_one' mode.")

        elif self.mode == QuestionModes.CHOOSE:
            if self.variants is None or not self.variants or not all(isinstance(variant, str) for variant in self.variants) or not isinstance(self.correct_answer, list) or not all(item in self.variants for item in self.correct_answer):
                raise ValueError("Invalid configuration for 'choose' mode.")

# # Example usage:
# if __name__ == '__main__':
#     question_input = Question(
#         title='Sample Input Question',
#         description='This is a sample input question.',
#         mode=QuestionModes.INPUT,
#         correct_answer='Sample Answer'
#     )

#     question_choose_one = Question(
#         title='Sample Choose One Question',
#         description='This is a sample choose one question.',
#         mode=QuestionModes.CHOOSE_ONE,
#         variants=['Option 1', 'Option 2', 'Option 3'],
#         correct_answer='Option 2'
#     )

#     question_choose = Question(
#         title='Sample Choose Question',
#         description='This is a sample choose question.',
#         mode=QuestionModes.CHOOSE,
#         variants=['Option A', 'Option B', 'Option C', 'Option D'],
#         correct_answer=['Option A', 'Option C']
#     )

#     question_input.set_user_answer('Sample Answer')
#     print(question_input.check_answer())  # Output: True

#     question_choose_one.set_user_answer('Option 2')
#     print(question_choose_one.check_answer())  # Output: True

#     question_choose.set_user_answer(['Option A', 'Option D'])
#     print(question_choose.check_answer())  # Output: False