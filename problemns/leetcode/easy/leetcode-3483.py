from itertools import permutations
from typing import List


class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        combinations = permutations(digits, 3)
        sett = set()
        count = 0
        for combo in combinations:
            strr = ""
            for i in combo:
                strr += str(i)
            if len(str(int(str(strr)))) != 3:
                continue
            if int(strr) % 2 == 0:
                sett.add(strr)
        return len(list(sett))
