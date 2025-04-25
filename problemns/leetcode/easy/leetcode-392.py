class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        i = 0
        j = 0
        string = ""
        while len(s) > 0 and i < len(t) and j < len(s):
            if t[i] == s[j]:
                string += s[j]
                j += 1
            i += 1
        return string == s
