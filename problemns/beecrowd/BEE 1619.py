n = int(input())

days_month = {"01": 31, "02": 28, "03": 31, "04": 30, "05": 31, "06": 30, "07": 31, "08": 31, "09": 30, "10": 31,
              "11": 30, "12": 31}
for i in range(n):
    data1, data2 = map(str, input().split())

    if data1 == data2:
        print(0)
        continue
    data_maior = max(data1, data2)
    data_menor = min(data1, data2)
    ano1, mes1, dia1 = data_maior.split("-")
    ano2, mes2, dia2 = data_menor.split("-")

    ano1 = int(ano1)
    ano2 = int(ano2)

    if (ano2 % 400 == 0) or (ano2 % 4 == 0 and ano2 % 100 != 0):
        days_month["02"] = 29
    else:
        days_month["02"] = 28
    summ = 0
    if ano1 == ano2:
        while mes2 != mes1:
            summ += days_month[mes2]
            mes2 = int(mes2)
            mes2 += 1
            if mes2 > 12:
                mes2 = 1
                ano2 += 1
            mes2 = str(mes2).zfill(2)
        summ = summ - int(dia2)
        summ = summ + int(dia1)
    else:
        while ano2 != ano1 or mes2 != mes1:
            summ += days_month[mes2]
            mes2 = int(mes2)
            if mes2 == 12:
                mes2 = "01"
                ano2 += 1
            else:
                mes2 += 1
                mes2 = str(mes2) if mes2 > 9 else "0" + str(mes2)
        summ = summ - int(dia2)
        summ = summ + int(dia1)
    print(summ)
# 2014-08-09 2014-05-23


'''
correct solution

from datetime import datetime

n = int(input())

for _ in range(n):
    data1, data2 = input().split()
    
    d1 = datetime.strptime(data1, "%Y-%m-%d")
    d2 = datetime.strptime(data2, "%Y-%m-%d")
    
    diferenca = abs((d1 - d2).days)
    
    print(diferenca)
'''

'''
4
2014-07-27 2014-07-25
2014-08-09 2014-05-23
2012-01-01 2013-01-01
1970-01-01 1970-01-01


Janeiro	31
Fevereiro	28 ou 29 (bissexto)
Março	31
Abril	30
Maio	31
Junho	30
Julho	31
Agosto	31
Setembro	30
Outubro	31
Novembro	30
Dezembro	31
'''
