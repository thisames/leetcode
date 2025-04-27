from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort()

        res = []
        i = 0
        while i < len(intervals):
            if i < len(intervals) - 1 and min(intervals[i + 1]) <= max(intervals[i]):
                listite = [intervals[i][0], intervals[i][1]]

                while i < len(intervals) - 1 and min(intervals[i + 1]) <= max(listite):
                    listite += intervals[i + 1]
                    i += 1
                listset = sorted(set(listite))
                res.append([listset[0], listset[-1]])
            else:
                res.append(intervals[i])
            i += 1
        return res
