numero = input()

numeros = []
string = ""

for i in range(len(numero)):
    if string == "":
        string += numero[i]

        for j in range(i, len(numero) - 1):
            string += "0"
        numeros.append(int(string))
        string = ""

notas = [100, 50, 20, 10, 5, 2, 1]

nota_100 = 0
nota_50 = 0
nota_20 = 0
nota_10 = 0
nota_5 = 0
nota_2 = 0
nota_1 = 0

for i in range(len(numeros)):
    while numeros[i] != 0:
        if numeros[i] - notas[0] >= 0:
            numeros[i] = numeros[i] - notas[0]
            nota_100 += 1
            continue
        if numeros[i] - notas[1] >= 0:
            numeros[i] = numeros[i] - notas[1]
            nota_50 += 1
            continue
        if numeros[i] - notas[2] >= 0:
            numeros[i] = numeros[i] - notas[2]
            nota_20 += 1
            continue
        if numeros[i] - notas[3] >= 0:
            numeros[i] = numeros[i] - notas[3]
            nota_10 += 1
            continue
        if numeros[i] - notas[4] >= 0:
            numeros[i] = numeros[i] - notas[4]
            nota_5 += 1
            continue
        if numeros[i] - notas[5] >= 0:
            numeros[i] = numeros[i] - notas[5]
            nota_2 += 1
            continue
        if numeros[i] - notas[6] >= 0:
            numeros[i] = numeros[i] - notas[6]
            nota_1 += 1
            continue

print(numero)
print(f"{nota_100} nota(s) de R$ 100,00")
print(f"{nota_50} nota(s) de R$ 50,00")
print(f"{nota_20} nota(s) de R$ 20,00")
print(f"{nota_10} nota(s) de R$ 10,00")
print(f"{nota_5} nota(s) de R$ 5,00")
print(f"{nota_2} nota(s) de R$ 2,00")
print(f"{nota_1} nota(s) de R$ 1,00")

# 1231234

# 1000000
# 200000
#  30000
#   1000
#    200
#     30
#      4
