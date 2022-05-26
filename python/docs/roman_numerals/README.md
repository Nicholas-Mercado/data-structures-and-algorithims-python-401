# Roman Numerals

The code challenges is to create a function that takes in Roman Numerals and returns its sum

## Approach & Efficiency

This function has a dictionary that keeps the value of each Roman Numeral. It iterates through each numeral checking whether it is smaller then the next numeral. If it is it subtracts the value form the total else it adds the value to the total.

## Big 0

Time Complexity --> O(n) beacuse it must iterate through every charater in the numeral.

[Code](python/code_challenges/roman_numerals.py)

[Tests](python/tests/code_challenges/test_roman_numerals.py)
