class Solution:
    def countAndSay(self, n: int) -> str:
        str1 = "1"
        string = ""
        for _ in range(1, n):
            i = 0
            while i < len(str1):
                count = 0
                if i != len(str1) - 1 and str1[i] == str1[i + 1]:
                    count += 1
                    while i != len(str1) - 1 and str1[i] == str1[i + 1]:
                        i += 1
                        count += 1
                    string += str(count) + str1[i]
                    i += 1
                else:
                    count += 1
                    string += str(count) + str1[i]
                    i += 1
            str1 = string
            string = ""
        return str1
