import string
from pprint import pprint


def main():
    words = [w for w in input().strip().split()]

    for i in range(len(words)):
        for ch in string.punctuation:
            words[i] = words[i].replace(ch, '')

    res = check(words)
    pprint(res)


def check(words):
    incorrect = list()
    used = [words[0]]

    for i in range(1, len(words)):
        if not used[-1].endswith(words[i][0]):
            incorrect.append(i + 1)
        else:
            if words[i] not in used:
                used.append(words[i])
            else:
                incorrect.append(i + 1)

    return incorrect