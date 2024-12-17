from idlelib.debugger_r import restart_subprocess_debugger
from pprint import pprint
from random import random, randrange


def learn(dataset: list[str]):
    """
    Function model learning

    :param dataset: List of str used for training. The text contains only lowercase Latin letters
    :return: data for function 'generate'
    """
    state = dict()
    state["first_word"] = list()

    for sentence in dataset:
        sentence = sentence.strip().split()
        state["first_word"].append(sentence[0])
        if sentence[0] not in state.keys():
            state[sentence[0]] = list()
        for i in range(1, len(sentence)):
            prev_word = sentence[i - 1]
            word = sentence[i]
            if word not in state.keys():
                state[word] = list()
            state[prev_word].append(word)

    return state


def generate(state) -> str:
    """
    Function generating random text

    :param state: Result form 'learn' function
    :return: str
    """
    result = list()
    result.append(state["first_word"][randrange(0, len(state["first_word"]))])
    word = result[-1]
    while state[word]:
        result.append(state[word][randrange(0, len(state[word]))])
        word = result[-1]
    return " ".join(result)


if __name__ == "__main__":
    pprint(generate(
        learn(["the dog ran across the field", "the cat chased across the field", "the dog jumped over the fence",
               "the cat jumped over the dog"])))
    pprint(generate(
        learn([
            "the dog ran quickly through the park chasing after a ball",
            "a ball rolled across the park as the kids quickly chased after it",
            "they quickly ran after the ball which flew across the park",
            "in the park the dog quickly grabbed the ball and ran off"
        ])))