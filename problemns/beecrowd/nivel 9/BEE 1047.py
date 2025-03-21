relogio = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]

entradas = [int(i) for i in input().split(" ")]

h1, m1, h2, m2 = entradas

if h1 == h2 and m2 > m1:
    tempo = m2 - m1
    print(f"O JOGO DUROU {0} HORA(S) E {tempo} MINUTO(S)")
else:
    i = relogio.index(h1)
    count = 0
    while i != h2:
        if relogio[i] == relogio[-1]:
            i = 0
            count += 1
            continue
        if relogio[i] != h2:
            count += 1
        i += 1

    if h1 == h2:
        count = 24

    hora = 60 * count
    tempo = hora + m2 - m1

    x = 60
    count = 0
    while True:
        if tempo >= x:
            x += 60
            count += 1
            continue
        else:
            break

    x = tempo - (count * 60)

    print(f"O JOGO DUROU {count} HORA(S) E {x} MINUTO(S)")
