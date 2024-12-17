import pytest

from solution.task_4 import pipeline


@pytest.mark.parametrize(
    "stages, details, expected",
    [
        ([1, 2, 3], [0, 6, 2], [6, 12, 9]),
        ([5, 5, 2], [6, 0, 7], [18, 12, 23]),
        ([5, 1, 10, 4], [3, 0, 4, 20], [30, 20, 40, 50])
    ]
)
def test(stages, details, expected):
    assert pipeline(stages, details) == expected