from collections import Counter
from typing import List


def majorityElement(nums: List[int]) -> int:
    num_freq = Counter(nums)

    number = 0
    for i in num_freq:
        if num_freq[i] > len(nums) / 2:
            number = i

    return number


print(majorityElement([2, 2, 1, 1, 1, 2, 2]))
