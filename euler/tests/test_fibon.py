from euler.fibon import less_than, n_first, nth


def test_less_than():
    assert(less_than(10) == [0, 1, 1, 2, 3, 5, 8])


def test_n_first():
    assert(n_first(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])


def test_nth():
    assert(nth(0) == 0)
    assert(nth(9) == 34)
