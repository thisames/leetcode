from typing import List

strs = ["flower", "flow", "flight"]


def longestCommonPrefix(strs: List[str]) -> str:
    string = ""
    for i in range(len(strs[0])):
        char = strs[0][i]
        for j in range(1, len(strs)):
            if i == len(strs[j]) or strs[j][i] != char:
                return string
        string += char
    return string


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


def longestCommonPrefix(strs):
    longest_pre = []

    if strs and len(strs) > 0:
        strs = sorted(strs)
        first, last = strs[0], strs[-1]
        for i in range(len(first)):
            if len(last) > i and last[i] == first[i]:
                longest_pre.append(last[i])
            else:
                return "".join(longest_pre)
    return "".join(longest_pre)


def func(strs):
    v = [len(string) for string in strs]
    x = min(v)

    index = 0
    while index < x:
        char = strs[0][index]
        for i in range(1, len(strs)):
            if char != strs[i][index]:
                return strs[0][:index]
        index += 1

    return strs[0]


print(longestCommonPrefix(["lower", "flow", "flight"]))
