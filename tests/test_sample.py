def add(a, b):
    return a + b


def test_add_works():
    assert add(2, 3) == 5


def test_add_fails_on_purpose():
    assert add(2, 2) == 5
