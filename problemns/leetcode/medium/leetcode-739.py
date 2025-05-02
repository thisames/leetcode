from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answers = [0] * len(temperatures)
        i = 0
        while i < len(temperatures):
            while stack and temperatures[i] > stack[-1][0]:
                answers[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            stack.append([temperatures[i], i])
            i += 1
        return answers
