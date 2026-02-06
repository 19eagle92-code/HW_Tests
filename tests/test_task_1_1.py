import pytest
from task_1_1 import discriminant, solution

params = ((1, 8, 15), (1, -13, 12), (-4, 28, -49))


@pytest.mark.parametrize("a,b,c", params)
def test_solution_(a, b, c):
    assert solution(a, b, c)


params1 = ((1, 1, 1))


@pytest.mark.parametrize("a,b,c", params1)
def test_diskriminant_пreater_than_or_equal_to(a, b, c):
    assert solution(a, b, c) is None


def test_all_zero_coefficients():
    """Тест, когда все коэффициенты равны нулю"""
    result = solution(0, 0, 0)
    # 0 = 0 - бесконечно много решений
    assert result is None
