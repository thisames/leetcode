string = "WWRRRWWWWWWRRRRRWRRWRRWR"

index = 0

while index < len(string):
    if string[index] == "W":
        count = 0
        while string[index] == "W" and index < len(string):
            count += 1
            index += 1
        print(count)
    else:
        index += 1
