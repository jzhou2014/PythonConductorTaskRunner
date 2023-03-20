# tests for the moneyify helper function

from helpers.moneyify import moneyify


def test_moneyify():
    assert moneyify(1) == "1.00"
    assert moneyify(1.11111111) == "1.11"
    assert moneyify("1") == "1.00"
    assert moneyify("11111.111111") == "11111.11"
