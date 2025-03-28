def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """

    i = 0
    j = m
    while i != n:
        nums1[j] = nums2[i]
        j += 1
        i += 1

    for i in range(len(nums1)):
        for j in range(len(nums1)):
            if nums1[i] < nums1[j]:
                ref = nums1[i]
                nums1[i] = nums1[j]
                nums1[j] = ref

    return nums1


print(merge([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3))
# print(merge([1], 1, [], 0))
