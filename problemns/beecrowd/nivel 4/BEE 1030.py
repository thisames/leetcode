nc = int(input())

for i in range(nc):
    entrada = [int(i) for i in input().split(" ")]
    n = entrada[0]
    k = entrada[1]

    lista = list(range(1, n + 1))
    mortos = set()

    index = lista.index(k)
    mortos.add(k)
    count = 0
    total_pular = k
    while len(mortos) != len(lista) - 1:
        if lista[index] in mortos and len(mortos) != 1:
            total_pular += 1
        if count == total_pular:
            mortos.add(lista[index])
            count = 0
            total_pular = k
        if index == len(lista) - 1:
            index = 0
            count += 1
            continue
        index += 1
        count += 1

    sobrou = 0
    for v in lista:
        if v not in mortos:
            sobrou = v
            break

    print(f"Case {i + 1}: {sobrou}")
