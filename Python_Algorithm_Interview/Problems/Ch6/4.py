import collections
from typing import List
import re


def my_sol(paragraph: str, banned: List[str]) -> str:
    # make seperated word list converted into lower case
    formatted_paragraph = []
    temp = ""
    for i in paragraph:
        if i.isalpha():
            temp += i
        elif temp != "":
            formatted_paragraph.append(temp.lower())
            temp = ""
        else:
            pass
    if temp != "":
        formatted_paragraph.append(temp.lower())
    word_count_dict = {}
    banned = [word.lower() for word in banned]

    for alphabet_list in formatted_paragraph:
        for word in alphabet_list:
            if not word.isalpha():
                alphabet_list.remove(word)

    for alphabet_list in formatted_paragraph:
        word = "".join(alphabet_list)
        if word == "" or word in banned:
            continue
        elif word not in word_count_dict:
            word_count_dict[word] = 1
        else:
            word_count_dict[word] += 1

    return max(word_count_dict, key=lambda x: word_count_dict[x])


def sol1(paragraph: str, banned: List[str]) -> str:
    words = [
        word
        for word in re.sub(r"[^\w]", " ", paragraph).lower().split()
        if word not in banned
    ]
    counts = collections.Counter(words)
    return counts.most_common(1)[0][0]
