quantidade = int(input())

for i in range(quantidade):
    t = int(input())
    ts = [int(i) for i in input().split(" ")]
    jumps = input()

    count = 0
    i = 0
    while i != len(jumps):
        if jumps[i] == "S" and ts[i] == 1 or jumps[i] == "S" and ts[i] == 2:
            count += 1

        if jumps[i] == "J" and ts[i] > 2:
            count += 1

        i += 1

    print(count)
