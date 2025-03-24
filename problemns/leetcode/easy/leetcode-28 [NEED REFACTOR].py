# Runtime 4ms
# bad code


def strStr(haystack, needle):
    if len(needle) > len(haystack):
        return -1

    if haystack == needle:
        return 0

    string = ""
    index = -1

    for i in range(len(haystack)):
        if haystack[i] == needle[0]:
            if needle == string:
                break
            count = 0
            for _ in haystack[i:]:
                count += 1
            if count >= len(needle):
                for j in range(len(needle)):
                    if string != needle[:j]:
                        string = ""
                        index = -1
                        break
                    a = haystack[i:][j]
                    b = needle[j]
                    if a == b:
                        if index == -1:
                            index = i
                        string += haystack[i:][j]
                    else:
                        string = ""
                        index = -1
                        break

    return index


print(strStr("aabaaadaaac", "aabaaac"))
