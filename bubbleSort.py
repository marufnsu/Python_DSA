arr = [9,8,7,6,10,18,3,2,1]
size = len(arr) - 1
count = 0
while size >= 0:
    for ind in range(size):
        if arr[ind + 1] < arr[ind]:
            min_index = ind + 1
            (arr[ind], arr[min_index]) = (arr[min_index], arr[ind])
            count += 1
        if count == 0:
            break
    size -= 1
print(arr)

