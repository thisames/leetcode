def createTargetArray(nums, index):
    target = []

    for i in range(len(nums)):
        value = nums[i]
        target.insert(index[i], value)

    return target


print(createTargetArray([0, 1, 2, 3, 4], [0, 1, 2, 2, 1]))
