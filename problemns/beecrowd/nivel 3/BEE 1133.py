x = int(input())
y = int(input())

menor = min(x, y)
maior = max(x, y)

for i in range(menor + 1, maior):
    if i % 5 == 2 or i % 5 == 3:
        print(i)
