from myfunc import subtraction
import pytest


#def test_subtraction_good():
 #   assert subtraction(10, 5) == 5

@pytest.mark.parametrize("a, b, expected_result", [(10, 5, 5),
                                                   (3, 7, -4),
                                                   (20, 1, 19),
                                                   (3, 0, 3)
                                                   ])
def test_subtraction_good(a, b, expected_result):
    assert subtraction(a, b) == expected_result


@pytest.mark.parametrize("expected_exception, minuend, subtrahend", [(TypeError, "4", 5),
                                                                     (TypeError, 7, "6"),
                                                                     ])
def test_subtraction_with_error(expected_exception, minuend, subtrahend):
    with pytest.raises(expected_exception):
        subtraction(minuend, subtrahend)