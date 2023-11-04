from ui import *
from sys import exit, argv
from icecream import ic


class Ui(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.start.clicked.connect(self.run)

    def run(self):
        if self.check.isChecked():
            self.desipher(self.input.text(), self.spin.value())
        else:
            self.sipher(self.input.text(), self.spin.value())

    def sipher(self, word, key):
        word = str(word).replace(" ", "")
        chars = dict()
        result = ""

        if key > len(word):
            key = key - (len(word) * (key // len(word)))

        if not key:
            self.output.clear()
            self.output.textCursor().insertText(word)
            return

        for i in range(key):
            chars[i] = list()

        for num in range(0, len(word), key):
            for i in range(key):
                if len(word) > num + i:
                    chars[i] += word[num + i]

        shiphred_list = list(chars.values())
        shiphred_list.reverse()

        for i in shiphred_list:
            result += "".join(i)

        self.output.clear()
        self.output.textCursor().insertText(result)

    def desipher(self, word, key):
        word = str(word).replace(" ", "")
        splited_word = list()
        result = []

        if key > len(word):
            key = key - (len(word) * (key // len(word)))

        if not key:
            self.output.clear()
            self.output.textCursor().insertText(word)
            return

        if len(word) % key:
            word_sep = len(word) // key + 1
        else:
            word_sep = len(word) // key

        for num in range(0, len(word), word_sep):
            buffer = []
            for i in range(word_sep):
                if len(word) > num + i:
                    buffer += word[num + i]
                    ic(num, i, buffer, word_sep)

            splited_word.append(buffer)
            ic(splited_word)
        splited_word.reverse()

        ic(splited_word)
        for num in range(word_sep):
            for el in splited_word:
                if len(el) > num:
                    result += el[num]

        result = "".join(result)

        self.output.clear()
        self.output.textCursor().insertText(result)

        print("#####")


if __name__ == "__main__":
    app = QApplication(argv)
    ui = Ui()
    ui.show()
    exit(app.exec_())
