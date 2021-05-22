from typing import *
import numpy as np

pair_dict = {}
words: List[str]


def choose_start() -> str:
    global words
    first_word = np.random.choice(words)
    while first_word.islower():
        first_word = np.random.choice(words)
    return first_word


def gen_story() -> str:
    gen_base()
    words_count = 100
    new_story = [choose_start()]
    for i in range(words_count):
        while new_story[-1] == words[-1]:
            new_story[-1] = np.random.choice(words)
        new_story.append(np.random.choice(pair_dict[new_story[-1]]))
    return " ".join(new_story)


def gen_base():
    global words
    global pair_dict
    with open("base.txt", encoding="utf8") as base_text:
        words = base_text.read().split()
        pairs = gen_pairs(words)
        for word, next_word in pairs:
            if word in pair_dict.keys():
                pair_dict[word].append(next_word)
            else:
                pair_dict[word] = [next_word]


def gen_pairs(base_list):
    for i in range(1, len(base_list)):
        yield base_list[i - 1], base_list[i]
