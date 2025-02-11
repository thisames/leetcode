while True:
    list_ = [int(i) for i in input().split(" ")]
    a, b = list_[0], list_[1]

    if a == 0 == b:
        break

    maior_list = set(map(int, input().split()))
    menor_list = set(map(int, input().split()))

    if menor_list == maior_list and len(maior_list) == 1:
        print(0)
        continue

    if len(menor_list) > len(maior_list):
        x = maior_list
        maior_list = menor_list
        menor_list = x

    menor_list = [valor for valor in menor_list if valor not in maior_list]

    print(len(menor_list))
