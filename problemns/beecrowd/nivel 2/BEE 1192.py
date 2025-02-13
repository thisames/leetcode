quantidade = int(input())

for i in range(quantidade):
    string = input()
    n1, letra, n2 = int(string[0]), string[1], int(string[2])

    if n1 == n2:
        print(n1 * n2)
        continue
    if letra.islower():
        print(n1 + n2)
    else:
        print(n2 - n1)
