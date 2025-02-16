entradas = [int(i) for i in input().split(" ")]

n, x = entradas

string = input()

entradas = [int(i) for i in input().split(" ")]

p, m, g = entradas

map = {"P": p, "M": m, "G": g}

i = 0
z = x
count = 0

torres_resto = []

while i != len(string):
    titan = string[i]
    titan_tamanho = map[titan]

    entrou_no_for = False
    for j in range(len(torres_resto)):
        if torres_resto[j] >= titan_tamanho:
            torres_resto[j] = torres_resto[j] - titan_tamanho
            entrou_no_for = True

    if entrou_no_for:
        if i == size:
            count += 1
        i += 1
        continue

    if x == titan_tamanho:
        count += 1
        x = z
        i += 1
        continue
    elif x > titan_tamanho:
        x = x - titan_tamanho
        size = len(string) - 1
        if i == size:
            count += 1
        i += 1
        continue
    elif x < titan_tamanho:
        count += 1
        torres_resto.append(x)
        x = z
        continue

print(count)
