import pytest

from solution.task_2 import check


@pytest.mark.parametrize(
    "n,expected",
    [
        (["book", "kangaroo", "tiger", "ocean", "nemo", "ocean"], [3, 6]),
        (["sunflower", "river", "river", "rabbit", "tree", "eagle", "tree"], [3, 7]),
        (["book", "king", "hook", "kangaroo", "hook"], [3, 4, 5])
    ]
)
def test(n, expected):
    assert check(n) == expected