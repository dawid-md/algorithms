def bubble(nums):
    z = len(nums)
    shuffled = True

    while shuffled:
        shuffled = False
        for j in range(1, z):
            if nums[j] < nums[j-1]:
                nums[j], nums[j-1] = nums[j-1], nums[j]
                shuffled = True
        z -= 1
    return nums

nums = [3,5,7,1,7,2,0,2,4]
print(bubble(nums))
