def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """

    if numRows == 1:
        return s

    matriz = []
    for i in range(numRows):
        linha = [""] * len(s)
        matriz.append(linha)

    i = 0
    j = 0
    count = 0
    ZIG = True
    ZAG = False
    while count != len(s):
        if i == 0 and ZAG:
            ZIG = True
            ZAG = False
            i += 1
        if i == numRows and ZIG:
            ZIG = False
            ZAG = True
            i -= 1
        if ZIG:
            matriz[i][j] = s[count]
            i += 1
        if ZAG:
            j += 1
            i -= 1
            matriz[i][j] = s[count]
        count += 1

    string = ""
    for i in matriz:
        for j in i:
            if j != "":
                string += j

    return string


# "PAYPALISHIRING"
# "PYAIHRIG"

print(convert("PAYPALISHIRING", 4))
