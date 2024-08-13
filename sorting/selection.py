def selectionsort(nums):
    currentitem = 0

    while currentitem < len(nums)-1:
        currentmin = currentitem
        for j in range(currentitem+1, len(nums)):
            if nums[j] < nums[currentmin]:
                currentmin = j
        nums[currentitem], nums[currentmin] = nums[currentmin], nums[currentitem]
        currentitem += 1

    return nums

nums = [2,0,1,4,2,1,7,3,0]
print(selectionsort(nums))