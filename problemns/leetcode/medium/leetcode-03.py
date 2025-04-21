# BEFORE HAVING LEARNED HASHMAP
class Solution(object):
    def lengthOfLongestSubstring(self, s):

        if len(s) == 0:
            return 0

        maior_string = ""

        i = 0
        j = 1
        string = s[i]
        while j != len(s):
            if s[j] in string:
                if len(string) > len(maior_string):
                    print(string, " ", maior_string)
                    maior_string = string
                i += 1
                j = i + 1
                string = s[i]
            else:
                string += s[j]
                j += 1

        if len(string) >= len(maior_string):
            maior_string = string

        return len(maior_string)


# AFTER HAD LEARNED HASHMAP
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = dict()

        over = 0
        count = 0
        i = 0
        j = 0
        while i < len(s):
            if s[i] not in hashmap:
                hashmap[s[i]] = i
                count += 1
                i += 1
            else:
                if count > over:
                    over = count
                count = 0
                hashmap.clear()
                j += 1
                i = j
        if count > over:
            over = count

        return over

# ANYWAY THE TWO SOLUTIONS STILL ARE WORST
