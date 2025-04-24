from collections import Counter
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        num_freq = Counter(nums)

        number = 0
        for i in num_freq:
            if num_freq[i] > len(nums) / 2:
                number = i

        return number


class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        if len(nums) < 2:
            return nums[0]

        nums.sort()

        i = 0
        count = 0
        current_count = 0
        value = None
        while i < len(nums) - 1:
            if i < len(nums) - 1 and nums[i] == nums[i + 1]:
                while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                    current_count += 1
                    i += 1
                current_count += 1
                if current_count > count:
                    count = current_count
                    value = nums[i]
                i += 1
                current_count = 0
                continue
            else:
                current_count += 1
                if current_count > count:
                    count = current_count
                    value = nums[i]
                i += 1
                current_count = 0

        return value


class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        if len(nums) < 2:
            return nums[0]

        current_count = 0
        first = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != first:
                current_count -= 1
            else:
                current_count += 1
            if current_count == -1:
                first = nums[i]
                current_count = 0
        return first
