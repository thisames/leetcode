entradas = [int(i) for i in input().split(" ")]

ld, cd, lv, cv = entradas

p = min(ld, cd)
q = min(lv, cv)

ans1 = max(p, q) * max(p, q)

min_sum = p + q

r = min(max(ld, cd), max(lv, cv))
s = min(min_sum, r)
ans2 = s * s

final = max(ans1, ans2)
print(final)
