list = [float(i) for i in input().split(" ")]

if list[0] < list[1] + list[2] and list[1] < list[0] + list[2] and list[2] < list[1] + list[0] :
    print(f"Perimetro = {(list[0] + list[1] + list[2])}")
else:
    print(f'Area = {((list[0] + list[1])/2) * list[2]}')

