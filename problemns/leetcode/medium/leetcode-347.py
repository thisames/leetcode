def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    numeros = []
    quantidades = []

    nums = sorted(nums)
    print(nums)

    i = 0
    while i != len(nums):
        quant = len([v for v in nums if v == nums[i]])
        numeros.append(nums[i])
        quantidades.append(quant)
        i += quant

    list = []

    for j in range(k):
        maior = 0
        index = 0
        for i in range(len(quantidades)):
            print(maior)
            if quantidades[i] > maior:
                maior = quantidades[i]
                index = i
        list.append(numeros[index])
        quantidades.pop(index)
        numeros.pop(index)

    return list


print(topKFrequent([1, 1, 1, 2, 2, 3], 2))
