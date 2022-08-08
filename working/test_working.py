from working import convert
import pytest


def test_basic():
    assert convert("10 AM to 10 PM") == "10:00 to 22:00"


def test_incorrect_hours():
    with pytest.raises(ValueError):
        convert("20 AM to 10 PM")
    with pytest.raises(ValueError):
        convert("00 AM to 00 PM")
    with pytest.raises(ValueError):
        convert("10 AM to 20 PM")
    with pytest.raises(ValueError):
        convert("20 AM to 20 PM")
    with pytest.raises(ValueError):
        convert("20:00 AM to 20 PM")
    with pytest.raises(ValueError):
        convert("20 AM to 20:00 PM")
    with pytest.raises(ValueError):
        convert("0 AM to 0 PM")
    with pytest.raises(ValueError):
        convert(" AM to 0 PM")



def test_incorrect_minutes():
    with pytest.raises(ValueError):
        convert("10:60 AM to 10 PM")
    with pytest.raises(ValueError):
        convert("10:00 AM to 10:60 PM")
    with pytest.raises(ValueError):
        convert("10:70 AM to 10 PM")
    with pytest.raises(ValueError):
        convert("10 AM to 10:70 PM")


def test_omits_to():
    with pytest.raises(ValueError):
        convert("10 AM 10 PM")
