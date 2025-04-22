from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        i = 0
        left = i + 1
        right = len(nums) - 1

        closest_sum = float('inf')
        min_diff = float('inf')

        while i < len(nums) - 2:
            if left >= right:
                i += 1
                left = i + 1
                right = len(nums) - 1
                continue

            current_sum = nums[i] + nums[left] + nums[right]
            current_diff = abs(target - current_sum)

            if current_diff < min_diff:
                min_diff = current_diff
                closest_sum = current_sum

            if current_sum > target:
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                return closest_sum

        return closest_sum


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()
        i = 0
        under = float('inf')
        v = float('inf')

        while i < len(nums) - 2:
            left = i + 1
            right = len(nums) - 1

            while left < right:

                summ = nums[i] + nums[left] + nums[right]
                calculate = abs(summ - target)

                if calculate < under:
                    under = calculate
                    v = summ

                if summ < target:
                    left += 1
                else:
                    right -= 1
            i += 1

        return v
