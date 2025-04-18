while True:
    a, c = map(int, input().split())
    if a == 0 == c:
        break

    heights = list(map(int, input().split()))
    count = 0
    i = 0
    compare = 1
    while i != a:
        j = 0
        while j < len(heights):
            if compare > heights[j]:
                if heights[j - 1]:
                    while j < len(heights) and compare > heights[j]:
                        j += 1
                    count += 1
            else:
                j += 1
        i += 1
        compare += 1
    print(count)

'''
5 8
1 2 3 2 0 3 4 5
3 3
1 0 2
4 3
4 4 1
0 0

'''
