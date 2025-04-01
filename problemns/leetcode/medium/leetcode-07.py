def reverse(x: int) -> int:
    if x > 0:
        string = str(x)[::-1]
        int_number = int(string)
        if -2 ** 31 <= int_number <= 2 ** 31:
            return int_number
        else:
            return 0
    else:
        string = str(x)[::-1].strip("-")
        int_number = -int(string)
        if -2 ** 31 <= int_number <= 2 ** 31:
            return int_number
        else:
            return 0


print(reverse(120))
