from jar import Jar
import pytest


def test_init():
    jar1 = Jar()
    assert jar1.capacity == 12

    jar2 = Jar(30)
    assert jar2.capacity == 30


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(10)
    with pytest.raises(ValueError):
        jar.deposit(20)


def test_withdraw():
    jar = Jar(10)
    jar.deposit(5)
    with pytest.raises(ValueError):
        jar.withdraw(6)
