# LISTA ENCADEADA CIRCULAR
while True:
    x = int(input())
    if x == 0:
        break
    entradas = [int(i) for i in input().split(" ")]
    if len(entradas) > x:
        break
    count = 0
    for i in range(len(entradas)):
        ANT = 0
        CURRENT = 0
        PROX = 0

        if i == 0:
            ANT = entradas[-1]
            CURRENT = entradas[i]
            PROX = entradas[i + 1]
        elif i == len(entradas) - 1:
            ANT = entradas[i - 1]
            CURRENT = entradas[i]
            PROX = entradas[0]
        else:
            ANT = entradas[i - 1]
            CURRENT = entradas[i]
            PROX = entradas[i + 1]

        if ANT < CURRENT > PROX or ANT < CURRENT > PROX or ANT > CURRENT < PROX:
            count += 1

    print(count)
