'''
Contains Duplicate
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example :
Input: nums = [1,2,3,1]
Output: true
'''

def contains_duplicate(nums):
    distinct_num = set(nums)
    if len(distinct_num) == len(nums):
        return False
    return True

'''
Altenative Solution:
def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
'''