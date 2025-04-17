n = int(input())

kg = []
prices = 0
price = []
kgs = 0
for i in range(1, n + 1):
    v = float(input())
    prices += v
    name = [i for i in input().split(" ")]
    print(f"day {i}: {len(name)} kg")
    price.append(v)
    kgs += len(name)
    kg.append(len(name))

mediaprice = prices / len(price)
mediakg = kgs / len(kg)
print(f"{mediakg:.2f} kg by day")
print(f"R$ {mediaprice:.2f} by day")

'''
3
9.58
Mamao Maca Melao
2.65
Melancia
9.54
Pera Uva Goiaba

'''
