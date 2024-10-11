from typing import List

strs = ["flower", "flow", "flight"]


def longestCommonPrefix(strs: List[str]) -> str:
    index = 0
    minLen = min([len(string) for string in strs])

    while index < minLen:
        char = strs[0][index]
        for i in range(1, len(strs)):
            if char != strs[i][index]:
                return strs[0][:index]
        index += 1
    return strs[0]


print(longestCommonPrefix(strs))
