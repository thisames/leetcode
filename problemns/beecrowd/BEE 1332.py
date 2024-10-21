N = int(input())

tamanho = 5
lista = [0] * N
for i in range(N):
    string = input()
    count = 0

    if len(string) > 4:
        lista[i] = 3
        continue

        notchar = ""
    for char in range(len("two")):
        if "two"[char] in string:
            count += 1
        else:
            notchar = "two"[char]
        if count == 2:
            if notchar not in "one":
                lista[i] = 2
                break
            else:
                lista[i] = 1
                break

for i in lista:
    print(i)

# two
# eoo
