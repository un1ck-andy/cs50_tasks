from numb3rs import validate
import pytest


def test_255():
    assert validate("1.1.1.1") == True
    assert validate("255.255.255.255") == True
    assert validate("256.255.255.255") == False
    assert validate("256.255.255.256") == False
    assert validate("255.256.255.255") == False





def test_alpha():
    assert validate("a") == False
    assert validate("255.255.255.a") == False

