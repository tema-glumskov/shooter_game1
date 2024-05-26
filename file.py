from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import *


class Question:
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3


# создаем список вопросов, сами вопросы, добавлем их в список
question_list = []
q1 = Question('Государственный язык Бразилии', 'Португальский', 'Английский', 'Бразильский', 'Испанский')
q2 = Question('Какого цвета нет на флаге России?', 'Зеленый', 'Белый', 'Синий', 'Красный')
q3 = Question('Национальная хижина якутов', 'Ураса', 'Юрта', 'Хата', 'Иглу')
q4 = Question('Какой остров самый большой в мире', 'Гренландия', 'Австралия', 'Россия', 'Антарктида')
q5 = Question('Самая населеная страна в мире', 'Китай', 'Индия', 'Сша', 'СССР')
q6 = Question('Сколько шататов в США', '50', '24', '32', '40')
q7 = Question('Самая длинная река в мире', 'Волга', 'Ока', 'Лена', 'Амазонка')

question_list.append(q1)
question_list.append(q2)
question_list.append(q3)
question_list.append(q4)
question_list.append(q5)
question_list.append(q6)
question_list.append(q7)

app = QApplication([])

window = QWidget()
window.setWindowTitle('Memory Card')
window.resize(400, 300)

btn_OK = QPushButton('Ответить')

lbl_question = QLabel('Самый сложный вопрос в мире')

RadioGroupBox = QGroupBox('Варианты ответов')
btn_1 = QRadioButton('Варианты 1')
btn_2 = QRadioButton('Варианты 2')
btn_3 = QRadioButton('Варианты 3')
btn_4 = QRadioButton('Варианты 4')

RadioGroup = QButtonGroup()

RadioGroup.addButton(btn_1)
RadioGroup.addButton(btn_2)
RadioGroup.addButton(btn_3)
RadioGroup.addButton(btn_4)

line_ans1 = QHBoxLayout()
line_ans2 = QHBoxLayout()
line_ans3 = QHBoxLayout()

line_ans2.addWidget(btn_1)
line_ans2.addWidget(btn_2)
line_ans3.addWidget(btn_3)
line_ans3.addWidget(btn_4)

line_ans1.addLayout(line_ans2)
line_ans1.addLayout(line_ans3)

RadioGroupBox.setLayout(line_ans1)
AnsGroupBox = QGroupBox('Результат теста')
lb_Result = QLabel('текст')
lb_Correct = QLabel('ответ')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result)
layout_res.addWidget(lb_Correct)
 
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lbl_question, alignment=(Qt.AlignCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)

AnsGroupBox.hide()
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.addStretch(5)


def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')


def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    btn_1.setChecked(False)
    btn_2.setChecked(False)
    btn_3.setChecked(False)
    btn_4.setChecked(False)
    RadioGroup.setExclusive(True)


answers = [btn_1, btn_2, btn_3, btn_4]


def ask(q):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lbl_question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()


def show_correct(res):
    lbl_question.setText(res)
    show_result()


def check_answers():
    if answers[0].isChecked():
        show_correct('Верно!')
        window.score += 1
        print(f'Статистика: \nВсего вопросов: {window.total}\nПравильных ответов: {window.score}')
        print(f'Рейтинг: {window.score / window.total * 100}%')
    elif answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
        show_correct('Неверно!')


def next_question():
    window.total += 1
    print(f'Статистика: \nВсего вопросов: {window.total}\nПравильных ответов:{window.score}')
    window.cur_question += 1
    if window.cur_question >= len(question_list):
        window.cur_question = 0
    q = question_list[window.cur_question]
    ask(q)


def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answers()
    else:
        next_question()


window.setLayout(layout_card)
window.setWindowTitle('Memory Card')
window.cur_question = -1

btn_OK.clicked.connect(click_OK)
window.score = 0
window.total = 0
next_question()
window.show()
app.exec()