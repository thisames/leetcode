list = [int(i) for i in input().split(" ")]

if list[1] % list[0] == 0 or list[0] % list[1] == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")