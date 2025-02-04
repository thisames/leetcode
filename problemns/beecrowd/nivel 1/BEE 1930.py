x = [int(i) for i in input().split(" ")]

count = 0
for i in range(len(x)):
    if len(x) -1 != i:
        count = count + (int(x[i]) - 1)
    else:
        count = count + int(x[i])

print(count)

