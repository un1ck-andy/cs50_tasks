from um import count
import pytest


def test_words():
    assert count("yummy") == 0

def test_case():
    assert count("HI UM") == 1