from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        if len(text) < 7:
            return 0
        target = set("balloon")
        text = [i for i in text if i in target]
        settext = set(text)

        if len(settext) < 5:
            return 0
        counter = Counter(text)
        values = list(counter.values())
        items = list(counter.keys())
        i = 0
        count = 0

        while True:
            if items[i] == "l" or items[i] == "o":
                if values[i] < 2:
                    break
            if values[i] <= 0:
                break
            if items[i] == "l" or items[i] == "o":
                values[i] -= 2
            else:
                values[i] -= 1
            if i == len(values) - 1:
                count += 1
                i = 0
                continue
            i += 1
        return count
