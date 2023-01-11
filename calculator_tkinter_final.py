from tkinter import *
from tkinter import messagebox
import math

'''Блок создания окна приложения'''

app = Tk()
app.title("Калькулятор Tkinter")  # Назначаем заголовок окну приложения
app.geometry("505x472")  # задаем размеры окна
app.resizable(False, False)  # запрещаем изменять размер
app.configure(bg='#1F2021')  # задаем фон окну

'''Блок объявления переменных'''

# Объявляем необходимые переменные
expression = StringVar(app, '0')  # поле ввода чисел и операций, по дефолту отображает 0
calculated = StringVar(app)  # поле вывода результата операций
full_stop = 1  # переменная нажатой точки
left_bracket = 0  # Позволяет понять поставлена ли левая скобка
for_calculation = None  # Переменная готовности данных для вычислений

'''Блок создания полей ввода/вывода значений'''

# создаем виджет ввода значений и вывода результата
# задаем параметры: выравнивание текста по правамо краю, цвет фона, щрифт, цвет символов, цвет фона для значения только для чтения,
# поле должно быть плоским, без рамки и только для чтения
expression_txt = Entry(app, textvariable=expression, justify=RIGHT, bg='#1F2021', font='Arial 15 bold', fg='#FFFFFF',
                       readonlybackground='#1F2021', relief=FLAT, bd=0, state='readonly')

# задаем следующие параметры: отступ от границы окна по оси Y, привязываем поле к СЕВЕРУ 'N', отступ от границы окна по оси X,
# поле должно растягиваться по оси X
expression_txt.pack(pady=5, anchor=N, padx=2, fill=X)

# аналогичные параметры задаем для поля вывода результата
calculated_lbl = Label(app, textvariable=calculated, anchor=E, bg='#1F2021', fg='#FFFFFF', font='Arial 20 bold',
                       relief=FLAT, bd=0)
calculated_lbl.pack(pady=5, anchor=N, padx=6, fill=X)

'''Блок логики работы калькулятора'''


# обьявляем функцию работы нашего калькулятора, которая принимает значения отданные Lambda функцией при нажатии кнопок
def calc(x):
    # ранее объявленные переменные - глобальные
    global full_stop
    global for_calculation
    global left_bracket
    # нажатие кнопки с цифрой добавляет значение в конец строки
    if x in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        if expression.get().startswith('0') and len(expression.get()) == 1:
            # если строка начинается с 0 и ее длина 1(то есть, это момент начала работы, на экране 0)
            expression.set('')  # убираем ноль и строка будет пустой
        # если длина строки < 25 и последние символы не возведение в квадрат и корень
        if len(expression.get()) < 25 and not expression.get().endswith(('\u00B2', '\u221a')):
            # то к концу строки добавляем цифру с нажатой кнопки
            expression.set(expression.get() + x)
    # если нажата точка
    elif x == '.':
        # если длина строки < 25 и переменная точки = 1 и последний символ строки не математическая оверация
        if len(expression.get()) < 25 and full_stop == 1 and not expression.get().endswith(
                ('+', '-', '*', '(', ')', '÷', '\u00B2', '\u221a')):
            expression.set(expression.get() + '.')  # к концу строки добаляем точку
            full_stop = 0  # и ставим переменную в 0, это запретит повторное добалнение точки
    # если нажат символ +
    elif x == '+':
        # если длина строки < 25 и последний символ строки не . и не (
        if len(expression.get()) < 25 and not expression.get().endswith(('.', '(')):
            # если последний символ +
            if expression.get().endswith('+'):
                expression.set(expression.get()[:-1] + '+')  # берем последний символ строки и заменяем на +
            # если последний символ -
            elif expression.get().endswith('-'):
                expression.set(expression.get()[:-1] + '+')  # берем последний символ строки и заменяем на +
            # если последний символ *
            elif expression.get().endswith('*'):
                expression.set(expression.get()[:-1] + '+')  # берем последний символ строки и заменяем на +
            # если последний символ ÷
            elif expression.get().endswith('÷'):
                expression.set(expression.get()[:-1] + '+')  # берем последний символ строки и заменяем на +
            else:
                expression.set(expression.get() + '+')  # иначе в конец строки добавляем +
            full_stop = 1  # а переменную нажатой точки ставим 1
    # аналогично нажатию +
    elif x == '-':
        if len(expression.get()) < 25 and not expression.get().endswith(('.', '(')):
            if expression.get().endswith('+'):
                expression.set(expression.get()[:-1] + '-')
            elif expression.get().endswith('-'):
                expression.set(expression.get()[:-1] + '-')
            elif expression.get().endswith('*'):
                expression.set(expression.get()[:-1] + '-')
            elif expression.get().endswith('÷'):
                expression.set(expression.get()[:-1] + '-')
            else:
                expression.set(expression.get() + '-')
            full_stop = 1
    # аналогично нажатию +
    elif x == '*':
        if len(expression.get()) < 25 and not expression.get().endswith(('.', '(')):
            if expression.get().endswith('+'):
                expression.set(expression.get()[:-1] + '*')
            elif expression.get().endswith('-'):
                expression.set(expression.get()[:-1] + '*')
            elif expression.get().endswith('*'):
                expression.set(expression.get()[:-1] + '*')
            elif expression.get().endswith('÷'):
                expression.set(expression.get()[:-1] + '*')
            else:
                expression.set(expression.get() + '*')
            full_stop = 1
    # аналогично нажатию +
    elif x == '÷':
        if len(expression.get()) < 25 and not expression.get().endswith(('.', '(')):
            if expression.get().endswith('+'):
                expression.set(expression.get()[:-1] + '÷')
            elif expression.get().endswith('-'):
                expression.set(expression.get()[:-1] + '÷')
            elif expression.get().endswith('*'):
                expression.set(expression.get()[:-1] + '÷')
            elif expression.get().endswith('÷'):
                expression.set(expression.get()[:-1] + '÷')
            else:
                expression.set(expression.get() + '÷')
            full_stop = 1
    # если нажат символ возведения в квадрат
    elif x == 'x\u00b2':
        # если длина строки < 25 и последний символ строки не .
        if len(expression.get()) < 25 and not expression.get().endswith('.') and not expression.get().endswith(
                #  и последний символ строки не квадрат и не корень, и не математическая операция
                ('\u00B2', '\u221a')) and not expression.get().endswith(('+', '-', '*', '÷', '(')):
            expression.set(expression.get() + '\u00B2')  # в конец строки добавляем возведение в квадрат
    # аналогично возведению в квадрат
    elif x == '\u221ax':
        if len(expression.get()) < 25 and not expression.get().endswith('.') and not expression.get().endswith(
                ('\u221a', '\u00B2')) and not expression.get().endswith(('+', '-', '*', '÷', '(')):
            expression.set(expression.get() + '\u221a')
    # если нажат символ числа pi
    elif x == '\u03C0':
        if expression.get().startswith('0') and len(expression.get()) == 1:
            # если строка начинается с 0 и ее длина 1(то есть, это момент начала работы, на экране 0)
            expression.set('')  # убираем ноль и строка будет пустой
        # если длина строки < 25 и последний символ строки не . не число или скобка, не символ возведения в квадрат и вычисление корня
        if len(expression.get()) < 25 and not expression.get().endswith('.') and not expression.get().endswith(
                ('\u221a', '\u00B2')) and not expression.get().endswith(
            (')', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9')):
            expression.set(expression.get() + str(math.pi))  # в конец строки добавляем число pi из функции math
    # если нажат символ C
    elif x == 'C':
        expression.set(expression.get()[:-1])  # убираем последний символ строки
        # если строка пуста записываем в нее 0
        if expression.get() == '':
            expression.set('0')
    # если нажат символ CE
    elif x == 'CE':
        expression.set('0')  # поле ввода значений ставим в 0
        for_calculation = None  # переменную готовности данных в None
        calculated.set('')  # поле вывода значений делаем пустым
    # если нажат символ +/-
    elif x == '\u00B1':
        # если длина строки < 25 и первый символ строки не 0 и не -
        if not expression.get().startswith('-') and not expression.get().startswith('0') and len(expression.get()) < 25:
            expression.set('-' + expression.get())  # добавляем - в начало строки
        # если строка уже начинается с -
        elif expression.get().startswith('-'):
            expression.set(expression.get()[1:])  # берем срез строки без первого символа и заменяем ее
    # если нажат символ (
    elif x == '(':
        # если строка начинается с 0
        if expression.get() == '0':
            expression.set('(')  # заменяем ноль на (
        else:
            if not expression.get().endswith(
            ('1', '2', '3', '4', '5', '6', '7', '8', '9')):
                expression.set(expression.get() + '(')  # иначе в конец строки добавляем (
        left_bracket += 1  # а к переменной добавляем 1
    # если нажат символ )
    elif x == ')':
        # если переменная не равна 0 и строка начинается не с 0
        if left_bracket != 0 and not expression.get() == '0' and not expression.get().endswith(('+', '-', '*', '÷')):
            expression.set(expression.get() + ')')# в конец строки добавляем (
            left_bracket -= 1 # а к переменной добавляем -1, это позволит числу ( соответствать числу )
    # если нажат символ =
    elif x == '=':
        try:
            # если строка не заканчивается на математичискую операцию
            if not expression.get().endswith(('+', '-', '*', '÷')):
                for_calculation = expression.get().replace('x', '*').replace('÷', '/').replace('\u00B2', '**2').replace(
                    '\u221a', '**0.5')  # replace позволить заменить символы которые мы использовали на понятные для функции EVAL
                calculated.set(eval(for_calculation)) # eval производит вычисления
            # если строка заканчивается на математичискую операцию
            elif expression.get().endswith(('+', '-', '*', '÷')):
                for_calculation = expression.get()[:-1].replace('x', '*').replace('÷', '/').replace('\u00B2', '**2').replace(
                    '\u221a', '**0.5')  # убираем последний символ строки
                calculated.set(eval(for_calculation))  # eval производит вычисления
            # делаем окпугление до целого числа, если ответ будет закончен на .0
            if str(calculated.get()[int(len(calculated.get()) - 2):]) == '.0':
                calculated.set(calculated.get()[:-2])
            expression.set('0')
        # исключение дкления на ноль
        except ZeroDivisionError:
            # вызываем окно с ошибкой
            messagebox.showerror('Внимание', 'Пора бы уже запомнить, что на ноль делить НЕЛЬЗЯ!!!')
            expression.set('0')  # поле ввода значений ставим на 0
            for_calculation = None  # Переменную готовности данных в None
            calculated.set('')  # поле вывода значений ставим пустым


'''Блок создания кнопок'''


# создаем фреймы для каждого ряда кнопок, объявляем функцию, где укажем нужные нам
# параметры кнопок. Создаем список с символами наших кнопок и пройдем по нему циклом, в отдельных случаях
# создадим кнопку вручную.

# объявление функции позволить прописывать меньше нужных нам значений при создании каждой кнопки
def button(parent, text, font, bg, fg, activebackground, activeforeground, width, pad=0):
    btn = Button(parent, text=text, font=font, bg=bg, fg=fg, activebackground=activebackground,
                 activeforeground=activeforeground, width=width, height=2, relief=FLAT, bd=0, padx=pad)
    return btn


# распределим кнопки по зонам
# создадим список со значениями символов на кнопках
zone_1 = [
    'CE', 'C', '(', ')',
]
btn_frame_1 = Frame(app, bg='#1F2021')  # создадим фрейм для первой зоны
# проходим циклом по списку символов и для каждого символа создаем кнопку, в которую и ложим наш символ
for digit in zone_1:
    btn = button(btn_frame_1, str(digit), 'Colibri 15 bold', '#2E333B', '#FFFFFF', '#383C42', '#CDCED0', 10)
    btn.config(command=lambda x=digit: calc(x))  # для команды нажатия кнопки используем Lambda функцию которая может
    # как принимать, так и отдавать значения
    btn.pack(side=LEFT, padx=1, pady=1, fill=BOTH)
btn_frame_1.pack(side=TOP, anchor=NW, padx=5, fill=BOTH)

# остальные зоны делаем аналогично первой, используем символы Unicode
zone_2 = [
    '\u03C0', 'x\u00b2', '\u221Ax', '÷',
]
btn_frame_2 = Frame(app, bg='#1F2021')
for digit in zone_2:
    btn = button(btn_frame_2, str(digit), 'Colibri 15 bold', '#2E333B', '#FFFFFF', '#383C42', '#CDCED0', 10)
    btn.config(command=lambda x=digit: calc(x))
    btn.pack(side=LEFT, padx=1, pady=1, fill=BOTH)
btn_frame_2.pack(side=TOP, anchor=NW, padx=5, fill=BOTH)

zone_3 = [
    '7', '8', '9',
]
btn_frame_3 = Frame(app, bg='#1F2021')
for digit in zone_3:
    btn = button(btn_frame_3, str(digit), 'Colibri 15 bold', '#383C42', '#FFFFFF', '#2E333B', '#CDCED0', 10)
    btn.config(command=lambda x=digit: calc(x))
    btn.pack(side=LEFT, padx=1, pady=1, fill=BOTH)

btn = button(btn_frame_3, '*', 'Colibri 15 bold', '#2E333B', '#FFFFFF', '#383C42', '#CDCED0', 10)
btn.config(command=lambda x='*': calc(x))
btn.pack(side=LEFT, padx=1, pady=1, fill=BOTH)
btn_frame_3.pack(side=TOP, anchor=NW, padx=5, fill=BOTH)

zone_4 = [
    '4', '5', '6',
]
btn_frame_4 = Frame(app, bg='#1F2021')
for digit in zone_4:
    btn = button(btn_frame_4, str(digit), 'Colibri 15 bold', '#383C42', '#FFFFFF', '#2E333B', '#CDCED0', 10)
    btn.config(command=lambda x=digit: calc(x))
    btn.pack(side=LEFT, padx=1, pady=1, fill=BOTH)

btn = button(btn_frame_4, '-', 'Colibri 15 bold', '#2E333B', '#FFFFFF', '#383C42', '#CDCED0', 10)
btn.config(command=lambda x='-': calc(x))
btn.pack(side=LEFT, padx=1, pady=1, fill=BOTH)
btn_frame_4.pack(side=TOP, anchor=NW, padx=5, fill=BOTH)

zone_5 = [
    '1', '2', '3',
]
btn_frame_5 = Frame(app, bg='#1F2021')
for digit in zone_5:
    btn = button(btn_frame_5, str(digit), 'Colibri 15 bold', '#383C42', '#FFFFFF', '#2E333B', '#CDCED0', 10)
    btn.config(command=lambda x=digit: calc(x))
    btn.pack(side=LEFT, padx=1, pady=1, fill=BOTH)

btn = button(btn_frame_5, '+', 'Colibri 15 bold', '#2E333B', '#FFFFFF', '#383C42', '#CDCED0', 10)
btn.config(command=lambda x='+': calc(x))
btn.pack(side=LEFT, padx=1, pady=1, fill=BOTH)
btn_frame_5.pack(side=TOP, anchor=NW, padx=5, fill=BOTH)

zone_6 = [
    '\u00B1', '0', '.',
]
btn_frame_6 = Frame(app, bg='#1F2021')
for digit in zone_6:
    btn = button(btn_frame_6, str(digit), 'Colibri 15 bold', '#383C42', '#FFFFFF', '#2E333B', '#CDCED0', 10)
    btn.config(command=lambda x=digit: calc(x))
    btn.pack(side=LEFT, padx=1, pady=1, fill=BOTH)

btn = button(btn_frame_6, '=', 'Colibri 15 bold', '#83CBD2', '#24393A', '#6DA9B0', '#466C71', 10)
btn.config(command=lambda x='=': calc(x))
btn.pack(side=LEFT, padx=1, pady=1, fill=BOTH)
btn_frame_6.pack(side=TOP, anchor=NW, padx=5, fill=BOTH)

app.mainloop()
