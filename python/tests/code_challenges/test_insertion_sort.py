import pytest
from code_challenges.insertion_sort import insertion_sort

def test_insertion_sort_full_sort():
    arr = [6,5,4,3,2,1]
    actual = insertion_sort(arr)
    expected = [1,2,3,4,5,6]
    assert actual == expected

def test_insertion_sort_reverse_sorted():
    arr = [20,18,12,8,5,-2]
    actual = insertion_sort(arr)
    expected = [-2,5,8,12,18,20]
    assert actual == expected

def test_insertion_sort_nearly_sorted():
    arr = [2,3,5,7,13,11]
    actual = insertion_sort(arr)
    expected = [2,3,5,7,11,13]
    assert actual == expected

def test_insertion_sort_empty():
    arr = []
    actual = insertion_sort(arr)
    expected = []
    assert actual == expected
