from typing import List


class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:

        over = float('inf')
        value = float('-inf')

        for i in nums:
            cal = abs(i - 0)
            if cal <= over:
                if cal == over:
                    if i > value:
                        value = i
                        over = cal
                        continue
                    continue
                value = i
                over = cal
        return value
