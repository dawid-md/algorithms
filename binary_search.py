def binary_search(x, nums):
    if len(nums) == 1:
        return x == nums[0]
    mid_index = len(nums) // 2
    if x == nums[mid_index]:
        return True
    elif x < nums[mid_index]:
        return binary_search(x, nums[:mid_index])
    elif x > nums[mid_index]:
        return binary_search(x, nums[mid_index:])


nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
# for item in nums:
#     print(binary_search(5, nums))

# print(binary_search(15, nums))

def binary_search_index(x, nums, left_index = 0, right_index = len(nums)):
    if left_index > right_index:
        return f'not found'
    mid_index = (left_index + right_index) // 2
    if x == nums[mid_index]:
        return f'found at index {mid_index}'
    elif x < nums[mid_index]:
        return binary_search_index(x, nums, left_index, mid_index-1)
    elif x > nums[mid_index]:
        return binary_search_index(x, nums, mid_index+1, right_index)

print(binary_search_index(-5, nums))

# for item in nums:
#     print(binary_search_index(item, nums))