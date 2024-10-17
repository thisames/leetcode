def fat(n):
    if n == 1:
        return 1
    else:
        return n * fat(n - 1)


def pares(n):
    if n == 0:
        print(n)
    else:
        if n % 2 == 0:
            print(n)
        return pares(n - 1)


# HEAD TAIL
def menor(list):
    print(list)
    if len(list) == 1:
        return list[0]
    else:
        if list[0] > list[1]:
            return menor(list[1:])
        else:
            list.pop(1)
            return menor(list)


def menor2(list):
    print(list)
    if len(list) == 1:
        return list[0]
    else:
        if list[0] > min(list):
            return menor2(list[1:])
        else:
            return list[0]


def menor3(list):
    if len(list) == 1:
        return list[0]
    else:
        t = len(list) // 2 - 1
        if menor3(list[0:t]) > menor3(list[len(list) // 2: len(list) - 1]):
            return menor3(list[0:(len(list) // 2) - 1])
        else:
            return menor3(list[len(list) // 2:len(list) - 1])


def menor4(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        menor_restante = menor(lista[1:])
        return lista[0] if lista[0] < menor_restante else menor_restante


def menor(lista):
    if len(lista) == 1:
        return lista[0]

    if not lista:
        return None

    meio = len(lista) // 2
    menor_esquerda = menor(lista[:meio])
    menor_direita = menor(lista[meio:])
    return menor_esquerda if menor_esquerda < menor_direita else menor_direita
