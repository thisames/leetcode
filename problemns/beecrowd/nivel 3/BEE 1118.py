def ler_nota():
    while True:
        nota = float(input())
        if 0 <= nota <= 10:
            return nota
        else:
            print("nota invalida")


def calcular_media():
    nota1 = ler_nota()
    nota2 = ler_nota()
    media = (nota1 + nota2) / 2
    print(f"media = {media:.2f}")


def novo_calculo():
    while True:
        print("novo calculo (1-sim 2-nao)")
        opcao = int(input())
        if opcao == 1 or opcao == 2:
            return opcao


while True:
    calcular_media()
    opcao = novo_calculo()
    if opcao == 2:
        break
