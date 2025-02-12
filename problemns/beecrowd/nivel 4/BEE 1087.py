tabuleiro = [[0 for _ in range(8)] for _ in range(8)]

for i in range(len(tabuleiro)):
    for j in range(len(tabuleiro[i])):
        tabuleiro[i][j] = f"{(j + 1)}-{i + 1}"

while True:
    list = [int(i) for i in input().split(" ")]

    X1 = list[0]
    Y1 = list[1]
    X2 = list[2]
    Y2 = list[3]

    if X1 == 0 and Y1 == 0 and X2 == 0 and Y2 == 0:
        break

    if X1 - X2 == 0 and Y1 - Y2 == 0:
        print(0)
        continue

    result = X1 - X2

    res = 0

    x = 0
    if result > 0:
        res = (X1 - result) - 1
        x = tabuleiro[Y1 - 1][res]
        if res >= len(tabuleiro):
            res = (X1 - result) - 1
            x = tabuleiro[Y1 - 1][res]
    else:
        res = (X1 - result) - 1
        x = tabuleiro[Y1 - 1][res]

    coord = f"{X2}-{Y2}"

    if x == coord:
        print(1)
        continue

    y_b = (Y1 - 1) - result
    if result < 0:
        y_b = (Y1 - 1) - abs(result)

    b = None

    if 0 < y_b < len(tabuleiro):
        b = tabuleiro[y_b][res]

    if b is not None and b == coord:
        print(1)
        continue

    y_a = (Y1 - 1) + result
    if result < 0:
        y_a = (Y1 - 1) + abs(result)

    a = None

    if 0 < y_a < len(tabuleiro):
        a = tabuleiro[y_a][res]

    if a is not None and a == coord:
        print(1)
        continue

    print(2)
