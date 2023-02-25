print("my variant--->", 15%3+1)


class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    def print(self):
        print(self.letters)

    def letters_num(self):
        return len(self.letters)
import string

class EngAlphabet(Alphabet):
    _letters_num = 26

    def __init__(self):
        super().__init__("En", string.ascii_uppercase)

    def is_en_letter(self, letter):
        return letter.upper() in self.letters

    def letters_num(self):
        return self._letters_num

    @staticmethod
    def example():
        return "Don't judge a book by it's cover."
eng_alphabet = EngAlphabet()
eng_alphabet.print()  # ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
print(eng_alphabet.letters_num())  # 26
print(eng_alphabet.is_en_letter('F'))  # True
print(eng_alphabet.is_en_letter('Щ'))  # False
print(EngAlphabet.example())  # "Don't judge a book by it's cover."
