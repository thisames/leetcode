import math

n, m, l, r = [int(i) for i in input().split(" ")]

list = []
for i in range(n):
    for j in range(m):
        list.append((i, j))
count = 0

i = 0
j = m
res = []
while i < len(list):
    res.append(list[i:j])
    i = j
    j += m

for i in range(len(list)):
    for j in range(i + 1, len(list)):
        x1, y1 = list[i]
        x2, y2 = list[j]

        dx = abs(x2 - x1)
        dy = abs(y2 - y1)

        far = math.sqrt(dx * dx + dy * dy)
        if l <= far <= r:
            if math.gcd(dx, dy) == 1:
                count += 1
print(count)
