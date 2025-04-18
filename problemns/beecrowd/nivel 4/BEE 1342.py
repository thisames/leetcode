while True:
    p, s = map(int, input().split())
    if p == 0 and s == 0:
        break

    trap = set([int(i) for i in input().split(" ")])
    n = int(input())

    players = {}
    for i in range(0, p):
        players[i] = [0, False]

    dados_result = []
    for i in range(n):
        d1, d2 = map(int, input().split())
        squad_sum = d1 + d2
        dados_result.append(squad_sum)

    i = 0
    j = 0
    while True:
        if i == p:
            i = 0
        if players[i][1] is False:
            players[i][0] += dados_result[j]
            if players[i][0] >= s + 1:
                print(i + 1)
                break
            if players[i][0] in trap:
                players[i][1] = True
            j += 1
        else:
            players[i][1] = False
        i += 1

'''
2 10
2 4 8
4
1 1
3 4
1 2
6 5
3 7
4 5 7
7
1 2
2 2
2 1
1 1
1 2
1 1
1 1

'''
