from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hashtable = dict()
        for x, y in points:
            cal = ((x - 0) ** 2) + ((y - 0) ** 2)
            if cal in hashtable:
                hashtable[cal].append([x, y])
            else:
                hashtable[cal] = [[x, y]]
        res = []
        hashtables = sorted(hashtable.keys())
        count = 0
        for i in hashtables:
            if count == k:
                break
            for j in hashtable[i]:
                res.append(j)
                count += 1
        return res
