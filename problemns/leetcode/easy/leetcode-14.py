from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        string = ""

        if len(strs) > 0 and strs[0] == "":
            return string

        if len(strs) == 1:
            return strs[0][0]

        i = 0
        j = 0
        while len(strs) > 0 and i < len(strs) - 1 and j < len(strs[i]) and j < len(strs[i + 1]) and strs[i][j] == \
                strs[i + 1][j]:
            if i + 1 == len(strs) - 1:
                string += strs[i][j]
                i = 0
                j += 1
                continue
            i += 1

        return string
