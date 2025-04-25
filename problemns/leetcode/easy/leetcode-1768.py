class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        string = ""
        i = 0
        j = 0
        while True:
            string += word1[i] + word2[j]
            if i == len(word1) - 1:
                string = string + word2[j + 1:]
                break
            if j == len(word2) - 1:
                string = string + word1[i + 1:]
                break
            i += 1
            j += 1
        return string
