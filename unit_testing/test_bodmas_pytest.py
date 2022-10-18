import bodmas


def test_addition():
    assert bodmas.addition(3, 1) == 4
    assert bodmas.addition(3, 7) == 10
    assert bodmas.addition(3, 1) == 4
    assert bodmas.addition(3, 4) == 7

def test_subtraction():
    assert bodmas.subtraction(3, 1) == 2
    assert bodmas.subtraction(5, 1) == 4
    assert bodmas.subtraction(6, 1) == 5


