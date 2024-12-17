from pprint import pprint


def main():
    try:
        n = int(input("Input n pulls > "))
    except:
        print("Incorrect type!")
        n = int(input("Input n pulls > "))

    res = pull(n)
    pprint(res)


def pull(n: int) -> tuple[int, int]:
    """
    :param n: num of pulls
    :return: tuple of 2 items: min count of 4 stars heroes, min count of 5 stars heroes.
    """

    tens = n // 10
    units = n % 10
    five_stars = 0
    four_stars = 0

    if tens < 1:
        return 0, 0
    else:
        five_stars = tens // 9
        four_stars = tens

        if not units:
            four_stars -= 1

    return four_stars, five_stars
