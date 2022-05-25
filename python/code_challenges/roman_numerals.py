def roman_numerals(roman):
    numerals_values = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1,}
    sum = 0
    for i in range(len(roman)):
        value = numerals_values[roman[i]]
        sum += value
    return sum
