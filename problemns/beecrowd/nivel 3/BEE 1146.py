while True:
    x = int(input())
    if x == 0:
        break

    string = ""
    for i in range(1, x + 1):
        if i != x:
            string += str(i) + " "
        else:
            string += str(i)
    print(string)
