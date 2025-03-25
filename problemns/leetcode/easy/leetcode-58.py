# Runtime 0ms
# good code

def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """

    count = 0
    for i in reversed(s.strip()):
        if i != " ":
            count += 1
        else:
            break

    return count


print(lengthOfLastWord("Hello World"))
