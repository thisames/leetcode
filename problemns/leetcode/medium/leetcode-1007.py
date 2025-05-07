from collections import Counter
from typing import List


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:

        over_top = Counter(tops).most_common(1)[0][0]
        over_bottoms = Counter(bottoms).most_common(1)[0][0]

        small = -1
        indexs = []

        top = True
        bot = True

        for i, v in enumerate(tops):
            if v != over_top:
                indexs.append(i)
        for i in indexs:
            if bottoms[i] != over_top:
                top = False
                break
        index1 = []

        for i, v in enumerate(bottoms):
            if v != over_bottoms:
                index1.append(i)
        for i in index1:
            if tops[i] != over_bottoms:
                bot = False
                break

        if top and bot:
            small = min(len(indexs), len(index1))
            return small
        if top and bot == False:
            return len(indexs)
        if bot and top == False:
            return len(index1)
        return small
