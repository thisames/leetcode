while True:
    try:
        string = input()
        process = int(input())
    except EOFError:
        break

    index = 0
    cicles = 0

    while index < len(string):
        if string[index] == "R":
            consecutivos = 0
            while index < len(string) and string[index] == "R" and consecutivos < process:
                index += 1
                consecutivos += 1
            cicles += 1
        else:
            cicles += 1
            index += 1

    print(cicles)
