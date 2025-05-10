from typing import List


def minSum(nums1: List[int], nums2: List[int]) -> int:
    summ = 0
    count_zero = 0
    summ2 = 0
    count_zero2 = 0
    if len(nums1) <= len(nums2):
        smallest = nums1
        biggest = nums2
    else:
        smallest = nums2
        biggest = nums1
    i = 0
    while i < len(biggest):
        if biggest[i] == 0:
            summ += 1
            count_zero += 1
        else:
            summ += biggest[i]

        if i < len(smallest):
            if smallest[i] == 0:
                summ2 += 1
                count_zero2 += 1
            else:
                summ2 += smallest[i]
        i += 1
    if summ2 == summ:
        return summ

    if summ2 > summ:
        if count_zero > 0:
            return summ2
        return -1

    if summ > summ2:
        if count_zero2 > 0:
            return summ
        return -1
    return -1


print(minSum([8, 13, 15, 18, 0, 18, 0, 0, 5, 20, 12, 27, 3, 14, 22, 0], [29, 1, 6, 0, 10, 24, 27, 17, 14, 13, 2, 19, 2, 11]))
