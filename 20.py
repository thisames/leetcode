s = "{[{{}]}"
s = "(){{}}"


def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    bracket_map = {')': '(', '}': '{', ']': '['}


print(isValid(s))
