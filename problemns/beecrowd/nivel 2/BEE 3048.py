x = int(input())

list = []
for i in range(x):
    n = int(input())
    list.append(n)

count = 0
for i in range(len(list)):
    if i == 0:
        count += 1
        continue
    if list[i] != list[i - 1]:
        count += 1

print(count)
