from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:

        prefix_max = []
        current_max = float('-inf')
        for num in nums:
            current_max = max(current_max, num)
            prefix_max.append(current_max)

        suffix_max = [0] * len(nums)
        current_max = float('-inf')

        for i in range(len(nums) - 1, -1, -1):
            current_max = max(current_max, nums[i])
            suffix_max[i] = current_max

        j = 1
        over = 0
        while j <= len(nums) - 2:
            print(j)
            calc = (prefix_max[j - 1] - nums[j]) * suffix_max[j + 1]
            if calc > over:
                over = calc
            j += 1

        return over if over > 0 else 0
