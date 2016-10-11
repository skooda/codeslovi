import random
from time import time

import pygments.lexers, pygments.formatters
from pygments import highlight
from fuzzywuzzy import fuzz
from flask import session
from unidecode import unidecode

from app.riddles import riddles


def __pretty_time(sec):
    min = sec // 60

    if not min:
        return "{0:.2f}s".format(sec)

    return "{0:.0f}m {1:.2f}s".format(min, sec % 60)


def __matchmake(count=5):
    choice = [i for i in range(0, len(riddles))]
    random.shuffle(choice)

    return choice[:count]


def __get_riddle_id(id):
    return session['choice'][id]


def __count_score(user_answer, correct_answers):
    answer_ascii = unidecode(user_answer).lower()
    answers = correct_answers

    max_score = 0
    for correct_answer in answers:
        score = fuzz.token_sort_ratio(answer_ascii, correct_answer)
        if score > max_score:
            max_score = score

    return max_score


def start():
    session['choice'] = __matchmake()
    session['start_time'] = time()
    session['penalties'] = 0


def end():
    session['end_time'] = time()


def get_hilighted_code(id):
    code = "<?php\n" + riddles[__get_riddle_id(id)]['code']

    return highlight(code, pygments.lexers.PhpLexer(), pygments.formatters.HtmlFormatter())


def is_answer_ok(answer, id):
    score = __count_score(answer, riddles[__get_riddle_id(id)]['answers'])
    return score >= 65  # Bulharská konstanta ;)


def save_answer(answer, id):
    if answer == "":
        session['penalties'] += 1

    session['answer' + str(id)] = answer


def get_total_time():
    return session['end_time'] - session['start_time'] + 60 * session['penalties']


def get_start_time():
    return session['start_time'] * 1000 - 60000 * session['penalties']


def get_pretty_time():
    return __pretty_time(get_total_time())


def get_answers():
    return [[session['answer' + str(i)], riddles[__get_riddle_id(i)]['text']] for i in range(0,5)]



