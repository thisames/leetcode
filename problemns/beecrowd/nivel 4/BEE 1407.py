from collections import Counter

while True:
    n, c, k = map(int, input().split())

    if n == 0 and c == 0 and k == 0:
        break

    numbers = []
    for _ in range(n):
        numbers += list(map(int, input().split()))

    not_there = []
    set_nums = set(numbers)
    for i in range(1, k + 1):
        if i not in set_nums:
            not_there.append(i)
    if len(not_there) > 0:
        not_there = sorted(not_there)
        print(' '.join(map(str, not_there)))
    else:
        under = float('inf')
        count = Counter(numbers)
        for i in count:
            if count[i] < under:
                under = count[i]
        results = []
        for i in count:
            if count[i] == under:
                results.append(i)
        results = sorted(results)
        print(' '.join(map(str, results)))

'''

5 4 6
6 2 3 4
3 4 6 5
2 3 6 5
4 5 2 6
2 3 6 4
4 3 4
3 2 1
2 1 4
4 3 2
1 4 3
0 0 0

'''
