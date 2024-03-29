#!/usr/bin/env python3
import prompt
from random import randint

# Количество раундов для победы
NUMBER_ROUNDS = 3


# Приветствует игрока
# Возвращает имя игрока
def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    return (name)


# Задать вопрос для игры Even
# Возвращает результат ответа
def qestions_game_even():
    number = randint(1, 100)
    answer = prompt.string('Question: ' + str(number) + ' ')
    correct_answer = 'yes' if number % 2 == 0 else 'no'
    print_answer(answer)
    if (answer == correct_answer):
        return True
    hint_not_correct(answer, correct_answer)
    return False


# Задать вопрос для игры Calc
# Возвращает результат ответа
def qestions_game_calc():
    number1 = randint(1, 50)
    number2 = randint(1, 50)
    math_op = randint(1, 3)
    correct_answer, operation = math_operation(number1, number2, math_op)
    answer = prompt.string('Question: ' + str(number1) + ' ' + operation + ' '
                           + str(number2) + ' ')
    print_answer(answer)
    if (answer == str(correct_answer)):
        return True
    hint_not_correct(answer, correct_answer)
    return False


# Задать вопрос для игры НОД (GCD)
# Возвращает результат ответа
def qestions_game_gcd():
    number1 = randint(1, 50)
    number2 = randint(1, 50)
    correct_answer = getGcd(number1, number2)
    answer = prompt.string('Question: ' + str(number1) + ' '
                           + str(number2) + ' ')
    print_answer(answer)
    if (answer == str(correct_answer)):
        return True
    hint_not_correct(answer, correct_answer)
    return False


# Задать вопрос для игры progression
# Возвращает результат ответа
def qestions_game_progression():
    PROG_LEN = 10
    prog = prog_gen(PROG_LEN, randint(1, 10), randint(1, 20))
    hide_number = randint(0, PROG_LEN - 1)
    correct_answer = prog[hide_number]
    prog[hide_number] = '..'
    answer = prompt.string('Question: ' + ' '.join(map(str, prog)) + ' ')
    print_answer(answer)
    if (answer == str(correct_answer)):
        return True
    hint_not_correct(answer, correct_answer)
    return False


# Задать вопрос для игры prime
# Возвращает результат ответа
def qestions_game_prime():
    number = randint(1, 100)
    answer = prompt.string('Question: ' + str(number) + ' ')
    correct_answer = 'yes' if is_prime(number) else 'no'
    print_answer(answer)
    if (answer == str(correct_answer)):
        return True
    hint_not_correct(answer, correct_answer)
    return False


# Проверяет является ли число простым
# если число простое то возвращается True
# если нет, то False
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True


# Генерирует арифметическую прогрессию длинной lenght,
# с шагом step, начиная с числа start
def prog_gen(lenght, step, start):
    progression = [(i * step) + start for i in range(lenght)]
    return (progression)


# Поиск максимального делителя двух чисел
# по алгоритму Евклида
def getGcd(a, b):
    while (a != 0) and (b != 0):
        if a > b:
            a = a - b
        else:
            b = b - a
    return (a + b)


'''
# Список натуральных делителей числа
def getDivs(a):
    divs = []
    for i in range(a):
        if a % (i + 1) == 0:
            divs.append(i + 1)
    return divs


# Поиск максимального делителя двух чисел
def getGcd(a, b):
    divs_a = getDivs(a)
    divs_b = getDivs(b)
    for i in reversed(divs_a):
        if i in divs_b:
            return i

'''


# Возвращает список с результатом математической операции
# и символ математической операции
def math_operation(number1, number2, math_op):
    result = []
    match math_op:
        case 1:
            result.append(number1 + number2)
            result.append('+')
        case 2:
            result.append(number1 - number2)
            result.append('-')
        case 3:
            result.append(number1 * number2)
            result.append('*')
    return (result)


# Выводит надпись при правильном ответе
def correct():
    print('Correct!')


# Выводит подсказку при неправильном ответе
def hint_not_correct(answer, correct_answer):
    print("'" + answer + "' is wrong answer ;(. Correct answer was '"
          + str(correct_answer) + "'.")


# Выводит финальную надпись при неправильном ответе
def not_correct(name):
    print("Let's try again, " + name + "!")


# Выводит надпись при поебеде игрока
def congrat(name):
    print('Congratulations, ' + name + '!')


# Выводит ответ игрока
def print_answer(answer):
    print('Your answer: ' + answer)
