import re


class Solution:
    def isPalindrome(self, s: str) -> bool:

        string = str(re.sub(r'[^a-zA-Z0-9]', '', s)).lower()

        if string == "":
            return True

        i = 0
        j = len(string) - 1
        while i < len(string) and i != j:
            if string[i] != string[j]:
                return False
            i += 1
            j -= 1
        return True
