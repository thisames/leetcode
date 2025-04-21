while True:
    n = int(input())
    
    if n == 0:
        break
    
    under = 100000000
    string = ""    
    for i in range(n):
        name, a, t = [i for i in input().split(" ")]
        a = int(a)
        t = int(t)
        cal = a - t
        if cal < under:
            under = cal
            string = name
    print(string)
