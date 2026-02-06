import pytest
from task_1_1 import discriminant, solution

params = ((1, 8, 15), (1, -13, 12), (-4, 28, -49))


@pytest.mark.parametrize("a,b,c", params)
def test_solution(a, b, c):
    assert solution(a, b, c)


def test_discriminant_less_zero():
    assert solution(1, 1, 1) is None
