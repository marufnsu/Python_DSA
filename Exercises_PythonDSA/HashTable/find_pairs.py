'''
Set: Find Pairs ( ** Interview Question)
You are given two lists of integers, arr1 and arr2, and a target integer value, target. Your task is to find all pairs of numbers (one from arr1 and one from arr2) whose sum equals target.

Write a function called find_pairs that takes in three arguments: arr1, arr2, and target, and returns a list of all such pairs. 
Assume that each array does not contain duplicate values.

Input
Your function should take in the following inputs:
arr1: a list of integers
arr2: a list of integers
target: an integer

Output
Your function should return a list of tuples, where each tuple contains two integers from arr1 and arr2 that add up to target.

Example 1:
arr1 = [1, 2, 3]
arr2 = [4, 5, 6]
target = 9

# Expected output: [(3, 6)]
'''

def find_pairs(arr1, arr2, target):
    result = []
    result_set = set(arr1)
    
    for num in arr2:
        compliment = target - num
        if compliment in result_set:
            result.append((compliment, num))
    return result


arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8, 10]
target = 7

pairs = find_pairs(arr1, arr2, target)
print (pairs)



"""
    EXPECTED OUTPUT:
    ----------------
    [(5, 2), (3, 4), (1, 6)]

"""