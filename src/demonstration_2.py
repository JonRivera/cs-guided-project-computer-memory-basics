"""
In order to solve this challenge you will need to [review the rules of Roman
Numerals](https://www.mathsisfun.com/roman-numerals.html).

Given a Roman Numeral (as a string), convert it to an integer. Your input is
guaranteed to be a Roman Numeral value from 1 to 3999. I ->3000 + 900+ 9 ->



Example 1:

Input: "IV"
Output: 4

Example 2:

Input: "XII"
Output: 12

Example 3:

Input: "MCMLXXXIV"
Output: 1984
"""


# Understand
# The objective here is to convert roman number into an integer
# The rules are that if first symbol(number) is larger or equal to the one that comes after then
# Take there sum, otherwise subtract the larger from the lower one and add the sum to some variable
# Plan
# Roman numerals are base on symbols ---> {I:1, V:5, X:10,L:50,C:100,D:500,M:1000}
# Iterate over the list of numbers
# check two roman numerals at a time
# if the first char is greater than the second one add the mappings based on the symbols dictionary together

def roman_to_integer(roman):


# ex of input: roman = "IV"
    symbols = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    index = 0
    while index < len(roman):
        if index == len(roman)-1:
            total += symbols[roman[index]]
            index += 1
        elif (index + 1 < len(roman)) and (symbols[roman[index]] >= symbols[roman[index + 1]]):
            total += symbols[roman[index]]
            index += 1 # skip to index after i + 1
        else:
            total +=  symbols[roman[index + 1]] - symbols[roman[index]]
            index += 2

    return total


# roman_integer = []
#
# if num % 1000 == 0:
#     num = num//1000
#     roman_num += *"M"
#


def roman_to_integer(roman):
    def roman_to_integer(roman):
        # Your code here
        mapping = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

    total = 0
    i = 0


# we'll want to look at roman numerals two-at-a-time
while i < len(roman):
    # subtractive case
    if i + 1 < len(roman) and mapping[roman[i]] < mapping[roman[i + 1]]:
        # if the left numeral < right numeral
        # subtract left from right
        diff = mapping[roman[i + 1]] - mapping[roman[i]]
        # add the result to our total
        total += diff
        # we need to skip both numerals
        i += 2
    # additive case
    else:
        # otherwise, left numeral >= right numeral
        # add the left numeral to our total
        total += mapping[roman[i]]
        i += 1

return total

print(roman_to_integer("MCMLXXXIV"))
