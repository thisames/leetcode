while True:
    string = input()

    if string == "*":
        break

    string_arr = string.upper().split(" ")
    first_letra = string_arr[0][0]

    find = False
    for i in string_arr:
        if i[0] != first_letra:
            find = True
            break
    if find:
        print("N")
    else:
        print("Y")
