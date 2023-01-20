nums = [7, 8, 1, 3, 4, 6, 7, 5]
nums2 = nums.copy()

print('\n', 'Input:', nums)

for i in range(len(nums2)):
    if i % 2:
        nums2[i] = nums2[i] * nums2[i] * nums2[i]
    else:
        nums2[i] = nums2[i] * nums2[i]

print('\n', 'Output:', nums2)
