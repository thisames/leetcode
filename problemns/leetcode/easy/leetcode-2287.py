from collections import Counter


class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:

        counter = Counter(s)

        count = 0
        i = 0
        while True:
            if counter[target[i]] <= 0:
                break
            if target[i] in counter:
                counter[target[i]] -= 1
            if i == len(target) - 1:
                i = 0
                count += 1
                continue
            i += 1
        return count
