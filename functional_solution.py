# Implement a function that will flatten and sort an array of integers in ascending order, and which adheres to a functional programming paradigm.

def flatten_and_sort(array):
    arr = []
    for item in array:
        for i in item:
            arr.append(i)
    return sorted(arr)

'''
Make sure to answer the following questions about your coding process:

How does this solution ensure data immutability?
--by making the solution a String which is an immutable data type

Is this solution a pure function? Why or why not?
--no, because it has the ability to change external data sets

Is this solution a higher order function? Why or why not?
--This is a higher order function because it contains a nested sorting function

Would it have been easier to solve this problem using a different programming style?
--no

Why in particular is functional programming a helpful paradigm when solving this problem?
--It simulates the real world entity. So real-world problems can be easily solved through oops
'''