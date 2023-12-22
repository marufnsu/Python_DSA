# Selection sort in Python
# time complexity O(n*n)
arr = [3,1,9,8,7,6,5,4]
size = len(arr)	
for ind in range(size):
	for j in range(ind + 1, size):
		# select the minimum element in every iteration
		if arr[j] < arr[ind]:
			min_index = j
	# swapping the elements to sort the array
	(arr[ind], arr[min_index]) = (arr[min_index], arr[ind])

print(arr)

