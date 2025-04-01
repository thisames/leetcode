from typing import List


def maxArea(height: List[int]) -> int:
    i = 0
    j = len(height) - 1

    maior = 0
    while i != j:
        altura = min(height[i], height[j])
        base = j - i
        if height[j] >= height[i]:
            i += 1
        else:
            j -= 1

        area = base * altura
        if area > maior:
            maior = area
    return maior


lista = [1, 8, 6, 2, 5, 4, 8, 3, 7]
lista = [1, 1]

print(maxArea(lista))
