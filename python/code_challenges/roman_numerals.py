def roman_numerals(roman):
    numerals_values = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1,}
    sum = 0
    for i in range(len(roman)):
        value = numerals_values[roman[i]]
        # i + 1 < len(roman) keeps [roman[i + 1]] string index in range
        if i + 1 < len(roman) and numerals_values[roman[i + 1]] > value:
            sum -= value
        else:
            sum += value
    return sum
