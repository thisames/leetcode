while True:
    try:
        x, y, m = map(int, input().split())
        cal = x * y
        for _ in range(m):
            x1, y1 = map(int, input().split())
            if x1 * y1 > cal:
                print("Nao")
            if x1 * y1 <= cal:
                print("Sim")
    except EOFError:
        break

'''
10 10 3
5 5
10 10
5 25
2 3 1
3 2

'''
