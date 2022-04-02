#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QPushButton, QApplication, QWidget, QRadioButton, QLabel, QHBoxLayout,QMessageBox,QVBoxLayout,QGroupBox,QButtonGroup
from random import randint, shuffle
app = QApplication([])
main_win = QWidget()
questions = []
rgb = QGroupBox('Варианты ответов')
class Question1():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
hmn = QGroupBox('Результаты')
btn_answer1 = QRadioButton('Энцы')
btn_answer2 = QRadioButton('Смурфы')
btn_answer3 = QRadioButton('Чулымцы')
btn_answer4 = QRadioButton('Алеуты')
text = QLabel('Какой национальности не существует?')
hgh = QPushButton('Ответить')
anwer = QLabel('Самый сложный вопрос в мире!')

a1=QLabel('Правильно\Неправильно')
a2=QLabel('Правильный ответ:')
#создание приложения и главного окна
 
#создание виджетов главного окна
 
radiogroup=QButtonGroup()
radiogroup.addButton(btn_answer1)
radiogroup.addButton(btn_answer2)
radiogroup.addButton(btn_answer3)
radiogroup.addButton(btn_answer4)
#расположение виджетов по лэйаутам
layouth1 = QHBoxLayout()
layouth2 = QVBoxLayout()
layouth3 = QVBoxLayout()
h4 = QVBoxLayout()
l4=QVBoxLayout()
layouth2.addWidget(btn_answer1, alignment = Qt.AlignCenter)
layouth2.addWidget(btn_answer2, alignment = Qt.AlignCenter)
layouth3.addWidget(btn_answer3, alignment = Qt.AlignCenter)
layouth3.addWidget(btn_answer4, alignment = Qt.AlignCenter)
layouth1.addLayout(layouth2)
layouth1.addLayout(layouth3)
rgb.setLayout(layouth1)

l4.addWidget(a1)
l4.addWidget(a2)
hmn.setLayout(l4)
rgb.show()
#обработка нажатий на переключатели
h4.addWidget(text)
h4.addWidget(rgb)
h4.addWidget(hmn)
h4.addWidget(hgh)
main_win.setLayout(h4)

#отображение окна приложения 
hmn.hide()
score=0
total=0
cur_question = 0



def show_result():
    rgb.hide()
    hmn.show()
    hgh.setText('Следующий вопрос:')
def show_question():
    hmn.hide()
    rgb.show()
    hgh.setText('Ответить')
    radiogroup.setExclusive(False)
    btn_answer1.setChecked(False)
    btn_answer2.setChecked(False)
    btn_answer3.setChecked(False)
    btn_answer4.setChecked(False)
    radiogroup.setExclusive(True)
def start_test():
    if hgh.text() == 'Следующий вопрос:':
        show_question()
    elif hgh.text() == 'Ответить':
        show_result()
answer=[btn_answer1,btn_answer2,btn_answer3,btn_answer4]
def ask(q : Question1):
    shuffle(answer)
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    text.setText(q.question)
    a2.setText(q.right_answer)
    show_question()
def show_correct(res):
    a1.setText(res)
    show_result()
def check_answer():
    global score
    if answer[0].isChecked():
        show_correct('Правильно!')
        score+=1
    elif answer[1].isChecked() or answer[2].isChecked() or answer[3].isChecked():
        show_correct('Неправильно):')
def next_question():
    global total
    total+=1
    cur_question = randint(0,len(questions)-1)
    if cur_question == len(questions):
        cur_question = 0
    ask(questions[cur_question])
def clivk_OK():
    if hgh.text()=='Ответить':
        check_answer()
    else:
        next_question()
def end():
    rgb.hide()
    hgh.hide()
'''if total == len(questions):
    end()'''
q1 = Question1('Сколько лет назад была ВОВ?','76','66','86','209')
q2 = Question1('Сколько дней в Феврале?','28','31','30','27')
q3 = Question1('Какой язык является основным в россии?','Русский','Российский','Старославянский','Пацанский')
q4 = Question1('Как называется зеленый пигмент в растениях?','Хлорофил','Хлерофол','Клоака','Электрон')
q5 = Question1('В каком возрасте наступает совершеннолетие?','18','16','14','21')
q6 = Question1('Самая длинная река в мире?','Амазонка','Ока','Волга','Москва-р')
q7 = Question1('Сколько длилась "Столетняя война" ?','116','100','107','98')
q8 = Question1('Cколько людей живёт на планете Земля ?','7 млрд','1 млрд','100 млн','5 млрд')
hgh.clicked.connect(clivk_OK)
questions.append(q1)
questions.append(q2)
questions.append(q3)
questions.append(q4)
questions.append(q5)
questions.append(q6)
questions.append(q7)
questions.append(q8)


    

main_win.setWindowTitle('Memory Card')
main_win.show()
app.exec_()
