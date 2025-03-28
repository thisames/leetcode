def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """

    if len(s) == 0:
        return 0

    maior_string = ""

    i = 0
    j = 1
    string = s[i]
    while j != len(s):
        if s[j] in string:
            if len(string) > len(maior_string):
                maior_string = string
            i += 1
            j = i + 1
            string = s[i]
        else:
            string += s[j]
            j += 1

    if len(string) >= len(maior_string):
        maior_string = string

    return len(maior_string)


string = "abcabcbb"
print(lengthOfLongestSubstring(string))
