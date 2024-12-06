from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    min_ = min(len(strs[0]), len(strs[-1]))

    index = 0

    while index < min_:
        char = strs[0][index]
        for i in range(1, len(strs)):
            if char != strs[i][index]:
                return strs[0][:index]
        index += 1
    return strs[0][:index]


def getLast(strs: List[str]) -> str:
    return strs[- 1]
    

def longestCommonPrefix2(strs: List[str]) -> str:
    strs = sorted(strs)
    result = ""
    first = strs[0]
    last = strs[-1]

    a = min(len(first), len(last))
    for i in range(min(len(first), len(last))):
        if first[i] != last[i]:
            return result
        result += first[i]
    return result


print(longestCommonPrefix2(["flower", "flow", "flight"]))
print(getLast(["flower", "flow", "flight"]))


# ["running", "jogging", "walking"]

def longestCommonSuffix(strs: List[str]) -> str:
    min_ = min([len(i) for i in strs])
    index = 0
    while index < min_:
        char = strs[0][len(strs[0]) - (1 + index)]
        for i in range(1, len(strs)):
            length = len(strs[i]) - (1 + index)
            if char != strs[i][length]:
                return strs[0][::-1][:index if index == 0 else length][::-1]
        index += 1
    return ""


def longestCommonSuffix(strs: List[str]) -> str:
    if not strs:
        return ""

    # Invertendo as strings para reaproveitar a lógica de prefixo comum
    reversed_strs = [s[::-1] for s in strs]
    min_len = min(len(s) for s in reversed_strs)

    index = 0
    while index < min_len:
        char = reversed_strs[0][index]
        for i in range(1, len(reversed_strs)):
            if reversed_strs[i][index] != char:
                return strs[0][-index:] if index > 0 else ""
        index += 1

    return strs[0][-index:]
