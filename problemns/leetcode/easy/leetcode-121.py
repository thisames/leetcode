from typing import List


class Solution:

    def compute_suffix_max(self, arr):
        n = len(arr)
        suffix_max = [0] * n
        suffix_max[-1] = arr[-1]

        for i in range(n - 2, -1, -1):
            suffix_max[i] = max(arr[i], suffix_max[i + 1])

        return suffix_max

    def maxProfit(self, prices: List[int]) -> int:
        suffix = self.compute_suffix_max(prices)
        over_profit = 0
        for i in range(len(prices) - 1):
            if prices[i] > suffix[i + 1]:
                continue
            cal = suffix[i + 1] - prices[i]
            if cal > over_profit:
                over_profit = cal
        return over_profit
