from typing import List


class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) < 1:
            return 0

        nums = sorted(set(nums))

        count_oficial = 0
        count_current = 0
        for i in range(len(nums) - 1):
            if nums[i] + 1 == nums[i + 1]:
                count_current += 1
            else:
                count_current += 1
                if count_current > count_oficial:
                    count_oficial = count_current
                count_current = 0

        count_current += 1
        count_oficial = max(count_oficial, count_current)
        return count_oficial
