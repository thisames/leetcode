# Runtime 0ms
# good performance, but very bad write, I make it when I was in class, I need refactor

def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    count = 0
    for i in range(0, n, 2):
        count += 1

    if n % 2 != 0:
        count -= 1

    root_list = []
    for i in range(count):
        root_list.append(2)

    if n % 2 != 0:
        root_list.append(1)

    root_list_copy = root_list

    result = 0

    two_quanty = root_list.count(2)
    one_quanty = root_list.count(1)

    maior = max(two_quanty, one_quanty)  # 2
    menor = min(two_quanty, one_quanty)

    # fatorial
    maior_count = maior
    for j in range(maior - 1, -1, -1):
        if j != 0:
            maior_count = maior_count * j

    menor_count = menor
    for j in range(menor - 1, -1, -1):
        if j != 0:
            menor_count = menor_count * j

    total_count = len(root_list_copy)
    for j in range(len(root_list_copy) - 1, -1, -1):
        if j != 0:
            total_count = total_count * j

    calc = 0
    if maior_count == 0 or menor_count == 0:
        result += 1
    else:
        res = maior_count * menor_count
        calc = total_count / res

    result += calc

    for i in range(len(root_list)):
        if root_list[i] == 2:
            root_list_copy[i] = 1
            root_list_copy.append(1)
            root_list_copy = root_list

            two_quanty = root_list_copy.count(2)
            one_quanty = root_list_copy.count(1)

            maior = max(two_quanty, one_quanty)  # 2
            menor = min(two_quanty, one_quanty)

            # fatorial
            maior_count = maior
            for j in range(maior - 1, -1, -1):
                if j != 0:
                    maior_count = maior_count * j

            menor_count = menor
            for j in range(menor - 1, -1, -1):
                if j != 0:
                    menor_count = menor_count * j

            total_count = len(root_list_copy)
            for j in range(len(root_list_copy) - 1, -1, -1):
                if j != 0:
                    total_count = total_count * j

            if maior_count == 0 or menor_count == 0:
                result += 1
                continue

            res = maior_count * menor_count
            calc = total_count / res
            result += calc

    return int(result)


print(climbStairs(14))

# 1 2 1 1
# 1 2 2
# 2 1 1 1
# 1 1 1 1 1
# 2 1 2

# 1 1 1 1
# 2 2
# 2 1 1
# 1 1 2
# 1 2 1

# 4! = 4 * 3 * 2 * 1 = 24/2 = 12

# 1 1 1
# 1 2
# 2 1

# 3! = 3 * 2 * 1

# 1 1
# 2
# 2! = 2 * 1
