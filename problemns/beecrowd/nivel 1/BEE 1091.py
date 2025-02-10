while True:
    n = int(input())
    if n == 0:
        break
    divisor_point = [int(i) for i in input().split(" ")]

    for i in range(n):
        coordinate = [int(i) for i in input().split(" ")]

        n = divisor_point[0]
        m = divisor_point[1]

        x = coordinate[0]
        y = coordinate[1]

        if x == n or x == m or y == n or y == m:
            print("divisa")
        elif x > n and y > m:
            print("NE")
        elif x > n and m >= y:
            print("SE")
        elif x <= n and m >= y:
            print("SO")
        elif x < n and m <= y:
            print("NO")
