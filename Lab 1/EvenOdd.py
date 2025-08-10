"""
First exercise: Check even/odd

Create a program with the following functions:
    - "createRandomList", that receives in input two numbers (N, R) and returns a list of N integer numbers with random values from 0 to R
    - "countEvenOdd", that given a list of numbers returns how many even and odd numbers contains
    - "splitEvenOdd", that given a list of numbers returns two lists, one containing the even numbers and the other the odd numbers
Test the program with N = 100 and R = 100
"""

import random
def createRandomList(N, R):
    mylist = []
    for i in range(N):
        mylist.insert(i, random.randint(0, R))
    return mylist

list1 = createRandomList(100, 100)
print(list1)

def countEvenOdd(l):
    num_odd = 0
    num_even = 0
    for i in range(len(l)):
        if l[i] % 2 == 0:
            num_even += 1
        else:
            num_odd += 1
    return f"{num_odd} odd number(s) and {num_even} even number(s)"

print(countEvenOdd(list1))

def splitEvenOdd(l):
    odd_list = []
    even_list = []
    for i in range(len(l)):
        if l[i] % 2 == 0:
            even_list.insert(i, l[i])
        else:
            odd_list.insert(i, l[i])
    return f"Odd number list = {odd_list}\nEven number list = {even_list}"

print(splitEvenOdd(list1))

