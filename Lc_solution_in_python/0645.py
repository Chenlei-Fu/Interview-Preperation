def findErrorNums(nums):
    """
    method 1: in-line changes
    time: O(n)
    space: O(1)
    """
    
    n = len(nums)
    res = []

    # find dups
    for i in range(n):
        idx = abs(nums[i]) - 1
        if nums[idx] >= 0:
            nums[idx] *= -1
        else:
            # nums[idx] < 0 -> the idx dup -> num dup
            res.append(abs(idx) + 1)

    # find loss
    for i, num in enumerate(nums):
        if num < 0: # have the number
            num = -num # restore
        else:
            res.append(i+1)
    return res

    """
    method 2: set
    return: [dup, loss]
    time: O(n)
    space: O(n)
    """
    # return [sum(nums) - sum(set(nums)), sum(set([i+1 for i in range(len(nums))])) - sum(set(nums))]
    





nums = [3,2,2]
print(findErrorNums(nums))


"""
test for method 1:
idx = 2 nums[2] = 2 -> [3, 2, -2]
idx = 1 nums[1] = 2 -> [3, -2, -2]
idx = 1 nums[1] = -2 -> res=[2]

num = 3 > 0 -> res = [2, 1]
"""
