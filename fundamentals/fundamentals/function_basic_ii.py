"""
Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
Example: countdown(5) should return [5,4,3,2,1,0]
"""
def countdown(x):
    new_list = []
    for i in range(x, -1, -1):
        new_list.append(i)
    return new_list
print(countdown(5))

"""
Create a function that will receive a list with two numbers. Print the first value and return the second.
Example: print_and_return([1,2]) should print 1 and return 2
"""
def print_and_return(ab):
    print(ab[0])
    return ab[1]
print(print_and_return([3,4]))

"""
Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)
"""
def first_plus_length(a):
    sum = len(a) + a[0]
    return sum
print(first_plus_length([2,2,3,4,5,6]))

"""
Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
Example: values_greater_than_second([3]) should return False
"""
def values_greater_than_second(b):
    newer_list = []
    if len(b) == 1:
        return False
    for i in range(len(b)):
        if b[1] < b[i]:
            newer_list.append(b[i])
            amount = len(newer_list)
    print(amount)
    return newer_list
print(values_greater_than_second([5,3]))

"""
Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
Example: length_and_value(4,7) should return [7,7,7,7]
Example: length_and_value(6,2) should return [2,2,2,2,2,2]
"""
def length_and_value(fixed_size, fixed_value):
    newest_list = []
    for i in range(fixed_size):
        newest_list.append(fixed_value)
    return newest_list
print(length_and_value(10,9))

