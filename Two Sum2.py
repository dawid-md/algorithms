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

# nums = [0,1,2,3,4]
# print(checker(nums, 3))


#function for checking if the sum is possible - each number could be used only once - solution is not returned
#brute force solution, not efficient for large lists, exponential time, function returns true if the first True is spotted
# def checker2(nums, target): 

#     for j in range(len(nums)):
#         if target - nums[j] == 0:
#             return True
#         elif target - nums[j] < 0 or nums[j] == 0:
#             continue
#         else:
#             nums2 = nums.copy()
#             nums2.pop(j)
#             if checker2(nums2, target - nums[j]) == True:
#                 return True

#     return False

# nums = [0,1,1,1]
# print(checker2(nums, 3))



# #solution from chatgpt - checks if each number in the list can be created using other numbers
# def checker3(nums, target):
#     # Create a boolean array of size (target + 1) to store achievable sums
#     dp = [False] * (target + 1) 
#     dp[0] = True  # Base case: target 0 is always achievable (with an empty subset) [True, False, False, False]
#         #array of size (target + 1)

#     for num in nums:
#         # Traverse backwards to avoid using the same number more than once
#         for t in range(target, num - 1, -1): #it skips numbers bigger than target!!
#             if dp[t - num]:
#                 dp[t] = True

#     return dp[target]

# nums = [2,1,3]
# print(checker3(nums, 4))


#function for checking if the sum is possible - returns first found solution, each number could be used only once
#brute force solution, not efficient for large lists, exponential time, function returns true if the first True is spotted
# def checker2(nums, target, firstSolution = None): 
#     if firstSolution is None:
#         firstSolution = []

#     for j in range(len(nums)):
#         if target - nums[j] == 0:
#             firstSolution.append(nums[j])   #it is required, otherwise item from the deepest level of recurrence will be missed
#             return True, firstSolution
#         elif target - nums[j] < 0 or nums[j] == 0:
#             continue
#         else:
#             nums2 = nums.copy()
#             nums2.pop(j)
#             flag, firstSolution = checker2(nums2, target - nums[j])
#             if flag == True:
#                 firstSolution.append(nums[j])
#                 return True, firstSolution

#     return False, []

# nums = [1,2,5]
# print(checker2(nums, 4))

#rekurencja dziala w ten sposob ze juz za pierwszym razem dochodzi do najglebszego poziomu jaki jest mozliwy dla danego elementu, sprawdza
 #pierwszy element, nastepnie dla tego pierwszego elementu sprawdza kombinacje z kolejnym elemente, nastepnie dla tej kombinacji sprawdza kombinacje z nastepnym elementem
 #gdy dochodzi do najglebszego poziomu to sprawdza na nim wszystkie elementy czy pasuja do kombinacji. Jezeli nie to wraca poziom wyzej, sprawdza kolejny element, 
 #nastepnie wchodzi znowu na najnizszy poziom dla tego kolejnego elementu i sprawdza dla niego kombinacje z kazdym pozostalym elementem
 #Jesli znajduje element pasujący do kombinacji to zaczyna się cofać do samego początku zwracając True i listę z danym elementem. 
 #Lista jest powiekszona 

def checker3(targetSum, numbers):
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None

    for num in numbers:
        remainder = targetSum - num
        pnumbers = numbers.copy()
        pnumbers.pop(0)
        solutionNumbers = checker3(remainder, pnumbers)
        if solutionNumbers != None and solutionNumbers != False:
            return [*solutionNumbers, num]

    return False


nums = [1,2,4]
# print(checker3(4, nums))

def checker4(targetSum, numbers):
    if targetSum == 0:
        return []
    if targetSum < 0:
        return False

    for j in range(len(numbers)):
        pnumbers = numbers.copy()
        currentNumber = pnumbers.pop(j)
        solutNumbers = checker4(targetSum - currentNumber, pnumbers)
        if solutNumbers != None and solutNumbers != False:
            return [*solutNumbers, currentNumber]
    
    return False

nums = [1,2,3,4,5,6,7,8,9,10,11]
print(checker4(70, nums))