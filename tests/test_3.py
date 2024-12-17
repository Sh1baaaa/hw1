import pytest

from solution.task_3 import learn


@pytest.mark.parametrize(
    "dataset,expected",
    [
        (["the dog ran across the field", "the cat chased across the field", "the dog jumped over the fence",
          "the cat jumped over the dog"], "the dog jumped over the dog ran across the field"),
        (["the dog ran quickly through the park chasing after a ball",
          "a ball rolled across the park as the kids quickly chased after it",
          "they quickly an after the ball which flew across the park",
          "in the park the dog quickly grabbed the ball and ran off"],
         "a ball rolled across the ball which flew across the dog ran off")
    ]
)
def test(dataset, expected):
    assert learn(dataset) == expected