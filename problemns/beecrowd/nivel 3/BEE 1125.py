while True:
    g_p = [int(i) for i in input().split(" ")]

    if g_p == [0, 0]:
        break

    g, p = g_p

    my_map = {}
    for i in range(1, p + 1):
        my_map[str(i)] = 0
    matriz = []

    for i in range(g):
        gs = [int(i) for i in input().split(" ")]
        matriz.append(gs)

    s = int(input())

    for j in range(s):
        ss = [int(j) for j in input().split(" ")]
        last_order_count = ss[0]
        points = ss[1:len(ss)]

        for colocaoes in matriz:
            gs = colocaoes[0:last_order_count]

            for x in range(len(colocaoes)):
                colocao = colocaoes[x]  # 10

                if colocao <= last_order_count and x <= len(points):
                    piloto = x + 1
                    my_map[str(piloto)] += points[colocao - 1]

        maior = 0
        index = None
        list_values_results = []
        for key, value in my_map.items():
            if value > maior:
                maior = value
                index = key

        if index is not None:
            list_values_results = [index]
            my_map.pop(index)

        for key, value in my_map.items():
            if value == maior:
                list_values_results.append(key)

        result = ' '.join(str(i) for i in list_values_results)
        print(result)
        my_map = {}
        for i in range(1, p + 1):
            my_map[str(i)] = 0
