x = int(input())

list = []
for i in range(x):
    list.append(input())

coelhos = 0
ratos = 0
sapos = 0
total = 0

for tipo in list:
    if "C" in tipo:
        tipos = int(tipo.split(" ")[0:-1][0])
        coelhos += tipos
    if "R" in tipo:
        tipos = int(tipo.split(" ")[0:-1][0])
        ratos += tipos
    if "S" in tipo:
        tipos = int(tipo.split(" ")[0:-1][0])
        sapos += tipos

total = coelhos + ratos + sapos

print(f"Total: {total} cobaias")
print(f"Total de coelhos: {coelhos}")
print(f"Total de ratos: {ratos}")
print(f"Total de sapos: {sapos}")
print(f"Percentual de coelhos: {(coelhos / total) * 100:.2f} %")
print(f"Percentual de ratos: {(ratos / total) * 100:.2f} %")
print(f"Percentual de sapos: {(sapos / total) * 100:.2f} %")
