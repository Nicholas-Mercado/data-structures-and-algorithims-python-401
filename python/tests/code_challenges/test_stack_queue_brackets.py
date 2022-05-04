import pytest
from code_challenges.stack_queue_brackets import multi_bracket_validation


# @pytest.mark.skip("TODO")
def test_validates_two_square_brackets():
    actual = multi_bracket_validation("[]")
    expected = True
    assert actual == expected

def test_validates_two_square_brackets_with_stuff():
    actual = multi_bracket_validation("[565464564645645gefsg]")
    expected = True
    assert actual == expected

def test_validates_two_square_brackets_with_space():
    actual = multi_bracket_validation("[     ]")
    expected = True
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_fails_two_square_brackets_flipped():
    actual = multi_bracket_validation("][")
    expected = False
    assert actual == expected

# @pytest.mark.skip("TODO")
def test_validates_one_bad_brace():
    actual = multi_bracket_validation("}")
    expected = False
    assert actual == expected

# @pytest.mark.skip("TODO")
def test_validates_two_braces():
    actual = multi_bracket_validation("{}")
    expected = True
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_fails_two_braces_flipped():
    actual = multi_bracket_validation("}{")
    expected = False
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_validates_two_parentheses():
    actual = multi_bracket_validation("()")
    expected = True
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_fails_two_parentheses_flipped():
    actual = multi_bracket_validation(")(")
    expected = False
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_multi():
    actual = multi_bracket_validation("{}(){}")
    expected = True
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_nested():
    actual = multi_bracket_validation("{([])}")
    expected = True
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_mismatched():
    actual = multi_bracket_validation("[}")
    expected = False
    assert actual == expected
