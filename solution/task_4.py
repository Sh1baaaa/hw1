from pprint import pprint
from xmlrpc.client import MAXINT


def pipeline(stages: list[int], details: list[int]) -> list[int]:
    """
    Conveyor function
    :param stages: A list of length n with the duration of processing of the part on each machine
    :param details: A list of length m with the arrival time of each part
    :return: A list of length m, which stores the time of complete processing of each part
    """
    global t, n, q, m, c, time, y
    t = stages
    n = len(t)
    y = [[0, 0]] * n

    q = details
    m = len(q)
    c = [0] * m

    timeline = list()
    time = 0

    while True:
        if y[-1][1] >= t[-1] and y[-1][0] != 0:
            c[y[-1][0] - 1] = time
            y[-1][0] = 0
        for i in range(n - 1, 0, -1):
            if y[i][0] == 0 and y[i - 1][1] >= t[i - 1]:
                y[i] = [y[i - 1][0], 0]
                y[i - 1][0] = 0
        if y[0][0] == 0:
            new_detail()
        timeline.append(tuple(y))
        time += 1
        for i in range(m):
            y[i][1] += 1

        if all(c[k] != 0 for k in range(m)):
            break
    return c


def new_detail():
    for j in range(m):
        if q[j] <= time:
            y[0] = [j + 1, 0]
            q[j] = MAXINT
            break
        else:
            y[0][0] = 0


if __name__ == "__main__":
    pprint(pipeline([5, 1, 10, 4], [3, 0, 4, 20]))