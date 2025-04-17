while True:
    n = int(input())
    if n == 0:
        break

    zonas = list(range(1, n + 1))
    saw = dict()
    trywhith = 4
    i = 0
    j = 0
    while len(saw) != n or list(saw)[-1] != 13:
        trywhith += 1
        saw = dict()
        count = 0
        while len(saw) != n:
            x = zonas[i]
            if zonas[i] not in saw:
                saw[zonas[i]] = count
            j = i + 1
            i = (i + trywhith) % len(zonas)
            if len(zonas[j:]) < trywhith:
                check = zonas[j:] + zonas[:i + 1]
                for c in check:
                    if c in saw:
                        i += 1
            else:
                check = zonas[j:i + 1]
                count = 0
                for c in check:
                    if c in saw:
                        count += 1
                while zonas[i] in saw:
                    i += 1
        print(list(saw.keys()))
