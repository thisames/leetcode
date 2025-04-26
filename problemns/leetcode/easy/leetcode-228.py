from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        i = 0
        res = []
        while len(nums) > 0 and i < len(nums):
            if i < len(nums) - 1 and nums[i] == nums[i + 1] - 1:
                current_str = nums[i]
                while i < len(nums) - 1 and nums[i] == nums[i + 1] - 1:
                    i += 1
                strr = f"{current_str}->{nums[i]}"
                res.append(strr)
                i = i + 1
            else:
                strr = str(nums[i])
                res.append(strr)
                i += 1
        return res
