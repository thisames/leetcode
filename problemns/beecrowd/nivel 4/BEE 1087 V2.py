while True:
    entrada = [int(i) for i in input().split(" ")]

    if entrada == [0, 0, 0, 0]:
        break

    x1, y1, x2, y2 = entrada[0], entrada[1], entrada[2], entrada[3]

    if x1 - x2 == 0 and y1 - y2 == 0:
        print(0)
    elif x1 - x2 == 0 or y1 - y2 == 0 or abs(x1 - x2) == abs(y1 - y2):
        print(1)
    else:
        print(2)
