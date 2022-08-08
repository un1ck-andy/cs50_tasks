from fuel import convert, gauge
import pytest


def test_convert():
    assert convert("3/4") == 75
    with pytest.raises(ValueError):
        convert("4/3")
    with pytest.raises(ZeroDivisionError):
        convert("4/0")


def test_gauge():
    assert gauge(1) == "E"
    assert gauge(100) == "F"
    assert gauge(50) == "50%"
    assert gauge(99) == "F"
    assert gauge(0) == "E"
