from plates import is_valid


def test_two_letters():
    assert is_valid("cs50") == True
    assert is_valid("50cs") == False
    assert is_valid("cs11") == True
    assert is_valid("55") == False


def test_length():
    assert is_valid("cs50andmore") == False
    assert is_valid("c") == False


def test_numbers_in_middle():
    assert is_valid("cs50o") == False


def test_first_number_not_0():
    assert is_valid("cs050") == False


def test_not_alpha():
        assert is_valid("best!") == False
