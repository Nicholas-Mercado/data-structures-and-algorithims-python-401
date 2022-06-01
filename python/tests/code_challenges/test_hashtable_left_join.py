import pytest
from code_challenges.hashtable_left_join import left_join


def test_exists():
    assert left_join


# @pytest.mark.skip("TODO")
def test_example():
    synonyms = {
        "diligent": "employed",
        "fond": "enamored",
        "guide": "usher",
        "outfit": "garb",
        "wrath": "anger",
    }
    antonyms = {
        "diligent": "idle",
        "fond": "averse",
        "guide": "follow",
        "flow": "jam",
        "wrath": "delight",
    }

    expected = [
        ["diligent", "employed", "idle"],
        ["fond", "enamored", "averse"],
        ["guide", "usher", "follow"],
        ["outfit", "garb", "NONE"],
        ["wrath", "anger", "delight"],
    ]

    actual = left_join(synonyms, antonyms)

    assert actual == expected


def test_all_None():
    synonyms = {
        "diligent": "employed",
        "fond": "enamored",
    }
    antonyms = {
        "flow": "jam",
        "wrath": "delight",

    }

    expected = [
        ["diligent", "employed", "NONE"],
        ["fond", "enamored", "NONE"],
    ]

    actual = left_join(synonyms, antonyms)

    assert actual == expected
