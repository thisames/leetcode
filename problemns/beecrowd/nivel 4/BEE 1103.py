relogio = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 0]

while True:
    list_times = [int(i) for i in input().split(" ")]

    h1 = list_times[0]
    m1 = list_times[1]
    h2 = list_times[2]
    m2 = list_times[3]

    if h1 == 0 and m1 == 0 and h2 == 0 and m2 == 0:
        break

    count = 1

    j = 0

    list_index_h1 = relogio.index(h1) + 1
    lenght = len(relogio) - 1

    if list_index_h1 > lenght:
        j = 0
    else:
        j = relogio.index(h1) + 1

    while relogio[j] != h2:
        if j == len(relogio) - 1:
            j = 0
            count += 1
            continue
        j += 1
        count += 1

    if count == 24 and m1 < m2:
        print(m2 - m1)
    else:
        print(((count * 60) - m1) + m2)
