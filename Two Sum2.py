def checker(nums, target):
    if target == 0:
        return True
    elif target < 0:
        return False

    for num in nums:
        if num == 0:
            continue
        if checker(nums, target - num) == True:
            return True
    
    return False

nums = [0,1,2,3,4]
print(checker(nums, 3))