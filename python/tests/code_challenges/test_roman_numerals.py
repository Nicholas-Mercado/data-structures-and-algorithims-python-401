import pytest
from code_challenges.roman_numerals import roman_numerals

def test_exists():
    assert roman_numerals

def test_only_add():
    roman = 'MDC'
    actual = roman_numerals(roman)
    expected = 1600
    assert actual == expected

def test_only_add_2():
    roman = 'MDCI'
    actual = roman_numerals(roman)
    expected = 1601
    assert actual == expected
