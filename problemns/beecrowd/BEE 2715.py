while True:
    try:
        num = int(input())
        todo = list(map(int, input().split()))
        under = float('-inf')
        i = 0
        left = sum(todo[0:i])
        right = sum(todo[i:])
        while i != len(todo):
            cal = abs(left - right)
            if cal < under:
                under = cal
                if under < 2:
                    break
            left += todo[i]
            right -= todo[i]
            i += 1

        print(under)
    except EOFError:
        break
'''
3
2 3 5
4
1 2 2 6

'''
