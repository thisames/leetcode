from collections import Counter

n = int(input())

for i in range(n):
    cards = list(map(int, input().split()))
    counter = Counter(cards)

    if len(cards) == 5 and len(counter) == 5:
        cardss = sorted(cards)
        ca = False
        for v in range(len(cardss) - 1):
            if cardss[v] != cardss[v + 1] - 1:
                ca = True
                break
        if ca is False:
            print(f"Teste {i + 1}")
            print(cardss[0] + 200)
            print("")
        else:
            print(f"Teste {i + 1}")
            print(0)
            print("")
    if len(counter) == 2:
        for j in counter:
            if counter[j] == 4:
                print(f"Teste {i + 1}")
                print(j + 180)
                print("")
                break
            if counter[j] == 3:
                print(f"Teste {i + 1}")
                print(j + 160)
                print("")
                break
    if len(counter) == 3:
        fi = False
        for j in counter:
            if counter[j] == 3:
                print(f"Teste {i + 1}")
                print(j + 140)
                print("")
                fi = True
                break
        if fi:
            continue
        pares = [chave for chave, valor in counter.items() if valor == 2]
        x, y = sorted(pares, reverse=True)
        sums = 3 * x + 2 * y + 20
        print(f"Teste {i + 1}")
        print(sums)
        print("")
    if len(counter) == 4:
        for chave, valor in counter.items():
            if valor == 2:
                print(f"Teste {i + 1}")
                print(chave)
                print("")
