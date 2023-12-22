nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n=3
nums1 = nums1[:m]
print(nums1)
nums2 = nums2[:n]
print(nums2)
mergedList = nums1 + nums2
print(mergedList)
nums1 = sorted(mergedList)
print(nums1)