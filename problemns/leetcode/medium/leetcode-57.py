from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        intervals.append(newInterval)

        intervals.sort()
        left, right = 0, 0
        result = []

        while right < len(intervals):
            current = intervals[left]

            while right < len(intervals) and intervals[right][0] <= current[1]:
                current[1] = max(intervals[right][1], current[1])
                right += 1

            result.append(current)
            left = right

        return result
