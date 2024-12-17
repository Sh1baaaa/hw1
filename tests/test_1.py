import pytest

from solution.task_1 import pull


@pytest.mark.parametrize(
    "n,expected",
    [
        (24, (2, 0)),
        (99, (9, 1)),
        (190, (18, 2)),
        (191, (19, 2))
    ]
)
def test(n, expected):
    assert pull(n) == expected