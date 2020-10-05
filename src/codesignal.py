"""PROBLEM#7 Even Digits Number"""
# A little boy is studying arithmetic. He has just learned how to add two integers,
# written one below another, column by column. But he always forgets about the important part - carrying.
#
# Given two integers, your task is to find the result which the little boy will get.
#
# Note: The boy had learned from this site, so feel free to check it
# out too if you are not familiar with column addition.
#
# Example
#
# For param1 = 456 and param2 = 1734, the output should be
# additionWithoutCarrying(param1, param2) = 1180.
#
#    456
#   1734
# + ____
#   1180
# The boy performs the following operations from right to left:
#
# 6 + 4 = 10 but he forgets about carrying the 1 and just writes down the 0 in the last column
# 5 + 3 = 8
# 4 + 7 = 11 but he forgets about the leading 1 and just writes down 1 under 4 and 7.
# There is no digit in the first number corresponding to the leading digit of the second one, so the boy imagine
# s that 0 is written before 456. Thus, he gets 0 + 1 = 1.


"""PLAN"""


# Understand, the boy for gets to cary a 1 whenever we add two digits whose sum is 10 or higher
# Plan:
# Add every two numbers per corresponding two the same index together and if the sume is greater than
#  subtract 10
# If the length is not the same then append a 0 to begining of that parm until all two param have equal length
# Need a way of splitting all numbers into individual numbers --> list comprehension
# Append a number at the start of the list array.insert(0,var)

def additionWithoutCarrying(param1, param2):
    # convert numbers into lists
    p1 = [int(p) for p in str(param1)]  # 1734 -> [1,7,3,4]
    p2 = [int(p) for p in str(param2)]  # 456 -> [4,5,6]
    p3 = []

    if len(p1) == len(p2):
        for index, number in enumerate(p2):
            sum1 = p1[index] + p2[index]
            print(sum1)
            if sum1 < 10:
                p3.append(sum1)
            # ensures the 1 isn't caried over in the sum
            else:
                p3.append(sum1 - 10)
    if len(p1) < len(p2):
        # padds 0s in the begging
        p1[:0] = [0] * (len(p2) - len(p1))
        for index, number in enumerate(p2):
            sum1 = p1[index] + p2[index]
            print(sum1)
            if sum1 < 10:
                p3.append(sum1)
            else:
                p3.append(sum1 - 10)
    elif len(p2) < len(p1):
        p2[:0] = [0] * (len(p1) - len(p2))
        for index, number in enumerate(p2):
            sum2 = p1[index] + p2[index]
            print(sum2)
            if sum2 < 10:
                p3.append(sum2)
            else:
                p3.append(sum2 - 10)
    total = [str(i) for i in p3]
    return int("".join(total))


""" PROBLEM#7 Even Digits Number"""


# Given an array of positive integers a, your task is to calculate how many of its elements have
# an even number of digits.
#
# Example
#
# For a = [12, 134, 111, 1111, 10], the output should be evenDigitsNumber(a) = 3.
#
# a[0] = 12 has 2 digits, which is an even number.
# a[1] = 134 has 3 digits, which is not an even number.
# a[2] = 111 has 3 digits, which is not an even number.
# a[3] = 1111 has 4 digits, which is an even number.
# a[4] = 10 has 2 digits, which is an even number.
# There are 3 elements (a[0], a[3], and a[4]) with an even number of digits, so the answer is 3.

# Understand
# Given an array of positive numbers how many of them are
# Even

# Plan
# loop over the list of numbers
# check that the digits are even per number, if evem
# use a counter to keep track of even elements, dicitonary can keep track.


def evenDigitsNumber(a):
    counter = 0
    for number in a:
        # checks if there an even #of digis
        if len(str(number)) % 2 == 0:
            counter += 1
    return counter


# TESTS
# Input:
# a: [7486, 1335, 80, 448, 275, 3569, 64, 942, 598, 6]
# Output:
# 5
# Expected Output:
# 5

# a: [1000, 10000, 10000]
# Output:
# 1
# Expected Output:
# 1

"""PROBLEM#9"""
# You are given a string strToSplit that consists of lowercase English letters only, and your task is to find the
# minimal number of good substrings you can split it into.
#
# Hint: Iterate over the string strToSplit and keep the ASCII codes of the smallest and the greatest characters in the current substring. Every time when
# the difference between them becomes greater than k, it means that the last considered symbol should be the first one in a new substring.
#
# Example
#
# For strToSplit = "aaabaaabb" and k = 0, the output should be goodSubstrings(strToSplit, k) = 4.
#
# strToSplit could be split into ["aaa", "b", "aaa", "bb"]. Each substring must consist of only one type of character, because
# it is required that |s[i] - s[j]| ≤ 0 for each substring s.

#[output] integer
#
# The minimal number of good substrings that the given string could be split into.

# Understand
# Want to know be able to split a string into good substring determine by k

# Plan
# Use ord(substring) to know the ASC2 code
# if the abs(difference(btw first char and second characters)) == <= k
# then save string into some ""
# else append string to some list, reset  dummy string, count+=1 continue loop

def goodSubstrings(strToSplit, k):
    # keep track of min and max unicode values (using ord function)
    # set min and max to be ord of the first char in the string
    smallest = ord(strToSplit[0])
    largest = ord(strToSplit[0])
    # we'll also need a count variable initialized to 1
    count = 1
    # iterate through the string
    for i in range(1,len(strToSplit)):
        # get the ord of the current char
        # update min or max as need be
        if(ord(strToSplit[i]) < smallest):
            smallest = ord(strToSplit[i])
        if (ord(strToSplit[i]) > largest):
            largest = ord(strToSplit[i])
        # get the diff of min and max (use the `abs` function)
        diff = abs(largest - smallest)
        # if diff > k
        # count += 1
        if diff > k:
            count += 1
            # reset our min and max to the be ord of the current char
            smallest = ord(strToSplit[i])
            largest = ord(strToSplit[i])
    return count



"""def goodSubstrings(strToSplit, k):
    count = 1
    start_ord = ord(strToSplit[0])
    for index, sub in enumerate(strToSplit):
        if abs(ord(sub) - start_ord) > k:
            count += 1
            print(sub)
            start_ord = ord(strToSplit[index])

    return count"""

#Failed Tests
# strToSplit: "fjgcfggdhihhdgedefhg"
# k: 3
# Output:
# 4
# Expected Output:
# 7
#
# Input:
# strToSplit: "hijjljjimgkjklgihjno"
# k: 5
# Output:
# 2
# Expected Output:
# 3
# Console Output:
# n

# Input:
# strToSplit: "hgmijmjmkiggnjnigmljnggmklljnhhihhjgiihnihmlkljjgg"
# k: 3
# Output:
# 17
# Expected Output:
# 19
# Console Output:
# m
# i
# m
# i
# n
# j
# n
# i
# m
# g
# m
# h
# n
# i
# m
# g