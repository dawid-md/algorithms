from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sol = []
        originalNums = nums.copy()
        nums.sort()
        n = 0
        m = len(nums)
        while n < m and nums[n] < target:
            n += 1
        nums = nums[:n]
        for j in range(len(nums)):
            for i in range(j + 1, len(nums)):
                if nums[j] + nums[i] == target:
                    sol.append(originalNums.index(nums[j]))
                    originalNums[sol[0]] = 'x'
                    sol.append()
                    return [originalNums.index(nums[j]), originalNums.index(nums[i])]

solution = Solution()

nums = [3,2,4]
target = 6

print(solution.twoSum(nums, target))