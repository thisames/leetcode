from collections import Counter


def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """

    counter = Counter(nums)

    list = []
    for num in counter:
        if counter[num] > len(nums) / 3:
            list.append(num)
    return list
