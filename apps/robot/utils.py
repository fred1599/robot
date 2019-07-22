from .words import WORDSLIST
from textwrap import wrap


def parse(question):
    words = [word for word in question.split() if word not in WORDSLIST]
    return words


def parse_text_wiki(d):
    res = ''
    for k in d:
        if 'extract' in d[k]:
            res += d[k]['extract']
    return wrap(res, width=70)
