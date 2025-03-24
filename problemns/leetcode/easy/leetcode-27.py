def removeElement(nums, val):
    count = 0
    length = len(nums) - 1
    i = 0
    while True:
        if i > length:
            break
        value = nums[i]
        if value != val:
            count += 1
            i += 1
        else:
            nums.pop(i)
            length -= 1

    return count


print(removeElement([3, 2, 2, 3], 3))
