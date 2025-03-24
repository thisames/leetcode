# Runtime 0ms
# good code
def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    value = 0
    for i in range(len(nums)):
        if target < nums[0]:
            return 0
        if nums[i] == target:
            return i
        if target > nums[i]:
            value = i

    return value + 1


print(searchInsert([1, 3, 5, 6], 0))
