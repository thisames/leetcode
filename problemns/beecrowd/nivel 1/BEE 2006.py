x = int(input())

n = [int(i) for i in input().split(" ")]

count = 0
for i in n:
    if i == x:
        count+=1

print(count)