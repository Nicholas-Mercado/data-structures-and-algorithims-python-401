import pytest
from data_structures.hashtable import Hashtable


def test_exists():
    assert Hashtable

def test_hash_create():
    ht = Hashtable()
    assert ht

def test_size_default():
    ht = Hashtable()
    actual = ht.size
    expected = 1024
    assert actual == expected

def test_hash():
    ht = Hashtable()
    index = ht.hash("cat")
    assert 0 <= index < ht.size

def test_hash_02():
    ht = Hashtable()
    index = ht.hash("at")
    assert 0 <= index < ht.size

# @pytest.mark.skip("TODO")
def test_set():
    ht = Hashtable()
    ht.set("color","blue")
    color_index = ht.hash("color")
    actual = ht.buckets[color_index]
    expected = ("color","blue")
    assert actual.head.value == expected
    
def test_collisions():
    ht = Hashtable()
    ht.set("cat", "Josie")
    ht.set("act", "A Contemporary Theater")
    ht.set("tac", "Taco Tuesday")

    assert ht.get("cat") == "Josie"
    assert ht.get("act") == "A Contemporary Theater"
    assert ht.get("tac") == "Taco Tuesday"

def test_get():
    ht = Hashtable()
    ht.set("color","blue")
    actual = ht.get("color")
    expected = "blue"
    assert actual == expected

@pytest.mark.skip("TODO")
def test_get_apple():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.get("apple")
    expected = "Used for apple sauce"
    assert actual == expected


@pytest.mark.skip("TODO")
def test_internals():
    hashtable = Hashtable(1024)
    hashtable.set("ahmad", 30)
    hashtable.set("silent", True)
    hashtable.set("listen", "to me")

    actual = []

    # NOTE: purposely breaking encapsulation to test the "internals" of Hashmap
    for item in hashtable._buckets:
        if item:
            actual.append(item.display())

    expected = [[["silent", True], ["listen", "to me"]], [["ahmad", 30]]]

    assert actual == expected
