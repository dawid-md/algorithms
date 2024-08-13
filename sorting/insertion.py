def insertion(nums):
    currentmin = 0
    currentitem = 1
    swapped = True

    while swapped == True:
        swapped = False
        for j in range(currentitem, len(nums)):
            if nums[j] < nums[currentmin]:
                currentmin = j
                swapped = True
        nums[currentitem], nums[currentmin] = nums[currentmin], nums[currentitem]

    return nums


nums = [2,1,3,0]
print(insertion(nums))