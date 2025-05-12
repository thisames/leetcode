from collections import Counter
from typing import List


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:

        counter = Counter(digits)
        copy = counter.copy()
        lis = []
        for i in range(99, 1000):
            if i % 2 != 0:
                continue
            strnumber = str(i)

            if strnumber[0] != '0' and int(strnumber[0]) in counter and counter[int(strnumber[0])] > 0:
                counter[int(strnumber[0])] -= 1
                if int(strnumber[1]) in counter and counter[int(strnumber[1])] > 0:
                    counter[int(strnumber[1])] -= 1
                    if int(strnumber[2]) in counter and counter[int(strnumber[2])] > 0:
                        counter[int(strnumber[2])] -= 1
                        lis.append(i)
            counter = copy.copy()
        return sorted(lis)
