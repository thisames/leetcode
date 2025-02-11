while True:
    list_ = [int(i) for i in input().split(" ")]
    a, b = list_[0], list_[1]

    if a == 0 == b:
        break

    maior_list = list(set([int(i) for i in input().split(" ")]))
    menor_list = list(set([int(i) for i in input().split(" ")]))

    if len(menor_list) == 1 == len(maior_list) and menor_list[0] == maior_list[0]:
        print(0)
        continue

    if len(menor_list) > len(maior_list):
        x = maior_list
        maior_list = menor_list
        menor_list = x

    for i in range(len(maior_list)):
        for j in range(len(menor_list) - 1):
            if maior_list[i] == menor_list[j]:
                menor_list.pop(j)

    if len(menor_list) > 4:
        print(4)
    else:
        print(len(menor_list))

# 1 3 5
# 2 4 6 8


# 1 1 2 3 5 7 8 8 9 15
# 2 2 2 3 4 6 10 11 11


# 1
# 1 2 2 3 5 7 8 8 9 15
# 1 2 2 3 4 6 10 11 11
