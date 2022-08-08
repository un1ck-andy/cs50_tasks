import seasons
import pytest


def test_print_minutes_words():
    assert (
        seasons.print_minutes_words(16760160)
        == "Sixteen million, seven hundred sixty thousand, one hundred sixty minutes"
    )
