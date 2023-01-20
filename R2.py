nums = [[2, 15, 4],
        [19, 24, 11],
        [7, 9, 5],
        [10, 3, 1]
        ]

print('Input:')
print('\n', nums[0], '\n', nums[1], '\n', nums[2], '\n', nums[3], '\n')

for i in range(len(nums)):
    for j in range(len(nums[i])):
        if j % 2:
                nums[i][j] = nums[i][j] * nums[i][j]

print('Output:')        
print('\n', nums[0], '\n', nums[1], '\n', nums[2], '\n', nums[3])
