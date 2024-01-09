import base64
import difflib

if __name__ == '__main__': print('question module')

class Question:
    def __init__(self,
                title='Это заголовок теста?',
                description='Возможно, это не тест...',
                image='путь/к/изображению',
                mode='input',
                variants=['да'],
                answer='правда',
                threshold_similarity=0.4,
                threshold_length_diff=2):
        
        self.qu_title = self.qu_format_string(title)
        self.qu_description = self.qu_format_string(description)
        self.qu_image_path = image
        self.qu_mode = mode
        self.qu_image_base64 = self.qu_image_to_base64(self.qu_image_path)
        self.qu_correct_answer = answer

        self.threshold_similarity = threshold_similarity
        self.threshold_length_diff = threshold_length_diff

        known_modes = ['choose_one', 'input']

        if self.qu_mode in known_modes:
            match self.qu_mode:
                case 'choose_one':
                    if not variants:
                        raise ValueError("Варианты не должны быть пустыми для режима 'choose_one'")
                    self.qu_variants = variants
                    if answer.lower() not in [variant.lower() for variant in variants]:
                        raise ValueError("Ответ должен быть одним из вариантов для режима 'choose_one'")

    def qu_format_string(self, string):
        string = string.capitalize()
        punctuation_marks = ['.', '!', '?']
        if not any(string.endswith(p) for p in punctuation_marks):
            string += "?"
        return string

    def qu_image_to_base64(self, image_path):
        try:
            with open(image_path, "rb") as img_file:
                img_bytes = img_file.read()
                img_base64 = base64.b64encode(img_bytes).decode('utf-8')
                return img_base64
        except FileNotFoundError:
            print("Файл не найден")

    def check_answer(self, user_answer):

        normalized_correct_answer = self.qu_correct_answer.lower()
        normalized_user_answer = user_answer.lower()
        diff_length = len(normalized_user_answer.split()) - len(normalized_correct_answer.split())
        diff_characters = len(normalized_user_answer) - len(normalized_correct_answer)
        similarity_ratio = difflib.SequenceMatcher(None, normalized_correct_answer, normalized_user_answer, autojunk=True).ratio()
        threshold_similarity = 0.4
        threshold_length_diff = 2
        return similarity_ratio >= threshold_similarity and abs(diff_length) <= threshold_length_diff and abs(diff_characters) <= threshold_length_diff