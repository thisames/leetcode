N = int(input())

# PCP - PC
# BBBE - I

for i in range(N):
    n_pessoas = int(input())
    list = []
    achou = False
    current_lang = ""
    for j in range(n_pessoas):
        lang = input()
        list.append(lang)
        if current_lang == "":
            current_lang = lang
        if len(list) > 1 and achou is False:
            if lang != list[0]:
                print("ingles")
                achou = True

    if achou is False:
        print(lang)
