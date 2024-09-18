import stuff, other_stuff


def test_stuff():
    assert stuff.multiply(3, 5) == 15
    assert stuff.multiply(3, "a") == "aaa"

def test_other_stuff():
    assert other_stuff.concatenate("abc", "def") == "abcdef"
