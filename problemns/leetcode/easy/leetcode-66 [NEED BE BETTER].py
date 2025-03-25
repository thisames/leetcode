# Runtime 1ms
# mid code

def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    string = ""
    for i in digits:
        string += str(i)

    number = [int(i) for i in list(str(int(string) + 1))]

    return number


print(plusOne([9]))
