list2 = [float(i) for i in input().split(" ")]

x = list2[0]
y = list2[1]

if x == 0 and y == 0:
    print("Origem")
elif x == 0:
    print("Eixo Y")
elif y == 0:
    print("Eixo X")
if x > 0 < y:
    print("Q1")
if x < 0 < y:
    print("Q2")
if y < 0 > x:
    print("Q3")
if y < 0 < x:
    print("Q4")