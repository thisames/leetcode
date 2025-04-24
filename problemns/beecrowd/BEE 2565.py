while True:
    try:
        n = int(input())
        l = []
        for i in range(n):
            m = float(input())
            l.append(m)
        l.sort()
        if n % 2 == 1:
            mediana = l[n // 2]
        else:
            mediana = (l[n // 2 - 1] + l[n // 2]) / 2
        count = 0.0
        for i in l:
            count += abs(mediana - i)
        print(f"{count:.2f}")
    except EOFError:
        break
'''
3
1.0
1.0
0.9
3
42.0
42.4
41.7

'''
