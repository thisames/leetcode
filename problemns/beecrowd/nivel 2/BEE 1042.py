list = [int(i) for i in input().split(" ")]

#[7, 21, -14]
#[7, 21, -14]

list2 = list.copy()

for i in range(len(list)):
    for j in range(len(list)):
        if list[i] < list[j]:
            n = list[i]
            list[i] = list[j]
            list[j] = n

for i in list:
    print(i)

print("")

for i in list2:
    print(i)

