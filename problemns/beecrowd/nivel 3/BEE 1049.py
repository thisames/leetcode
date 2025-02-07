list = []
for i in range(3):
    list.append(input())

if list[0] == "vertebrado":
    if list[1] == "ave":
        if list[2] == "carnivoro":
            print("aguia")
        else:
            print("pomba")
    else:
        if list[2] == "onivoro":
            print("homem")
        else:
            print("vaca")
else:
    if list[1] == "inseto":
        if list[2] == "hematofago":
            print("pulga")
        else:
            print("lagarta")
    else:
        if list[2] == "hematofago":
            print("sanguessuga")
        else:
            print("minhoca")
