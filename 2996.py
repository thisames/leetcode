from typing import List


# [4,5,6,2,5,6,7,8,15,17,18]
def missingInteger(nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0] + 1

    sum_ = nums[0]
    for i in range(0, len(nums) - 1):
        if nums[i] == nums[i + 1] - 1:
            sum_ += nums[i]
        else:
            if sum_ > nums[0]:
                sum_ += nums[i]
                break

        if nums[i] == nums[len(nums) - 2]:
            if nums[i] == nums[i + 1] - 1:
                sum_ += nums[i + 1]
                break

    if sum_ in nums:
        return max(nums) + 1
    else:
        return sum_


print(missingInteger([37, 1, 2, 9, 5, 8, 5, 2, 9, 4]))

c = 0
for i in [29, 30, 31, 32, 33, 34, 35, 36, 37]:
    c += i

print(c)
