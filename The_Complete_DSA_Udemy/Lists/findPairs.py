'''
Pairs
Write a function to find all pairs of an integer array whose sum is equal to a given number. Do not consider commutative pairs.

Example
pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7)
Output : ['2+5', '4+3', '3+4', '-2+9']

Note:
4+3 comes from second and third elements from the main list.
3+4 comes from third and seventh elements from the main list.
'''
def pair_sum(arr, target_sum):
    result = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target_sum:
                result.append(f"{arr[i]}+{arr[j]}")
    return result

'''
Alternative Solution:
def pair_sum(myList, sum):
    output = []
    
    for num in myList:
        target = sum - num
        idx = myList.index(num)
        if target in myList[idx:]:
            pairs = f'{num}+{target}'
            if pairs in output:
                continue
            else:
                output.append(pairs)
    return output
'''