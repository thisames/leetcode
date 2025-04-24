magic_data = {
    "fire": {"Dano": 200, 1: 20, 2: 30, 3: 50},
    "water": {"Dano": 300, 1: 10, 2: 25, 3: 40},
    "earth": {"Dano": 400, 1: 25, 2: 55, 3: 70},
    "air": {"Dano": 100, 1: 18, 2: 38, 3: 60}
}

T = int(input())

for _ in range(T):
    w, h, x0, y0 = map(int, input().split())
    spell_info = input().split()
    magia = spell_info[0]
    nivel = int(spell_info[1])
    cx, cy = map(int, spell_info[2:])

    raio = magic_data[magia][nivel]
    dano = magic_data[magia]["Dano"]

    px = max(x0, min(cx, x0 + w))
    py = max(y0, min(cy, y0 + h))

    dist_sq = (px - cx) ** 2 + (py - cy) ** 2

    if dist_sq <= raio ** 2:
        print(dano)
    else:
        print(0)

'''
4
10 10 50 50
fire 1 85 55
10 10 50 50
fire 2 85 55
10 10 50 100
water 3 100 100
10 10 50 100
air 3 100 100

'''
