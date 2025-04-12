x = int(input())
s = list(input())

i = 0
c = 0
cm = 0
cw = 0
cmb = False
cwb = False
count = 0
while i != len(s):
    if s[i] == "W":
        cw += 1
        cwb = True
    if s[i] == "M":
        cm += 1
        cmb = True
    if abs(cm - cw) > x:
        if s[i] != s[i + 1]:
            ref = s[i]
            s[i] = s[i + 1]
            s[i + 1] = ref
            if cwb:
                cw -= 1
            if cmb:
                cm -= 1
            continue
        else:
            break
    else:
        count += 1
    i += 1
    cmb = False
    cwb = False

print(count)
