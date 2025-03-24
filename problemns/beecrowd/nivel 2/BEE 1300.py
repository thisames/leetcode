angulo = int(input())

ponteiro_hora = 0
ponteiro_minuto = 0
achou = False
hora = 0

count = 0
while ponteiro_hora != 120:
    count += 1
    ponteiro_minuto += 1
    if count == 12:
        hora += 1
        ponteiro_hora += 1
        count = 0
    x = ponteiro_minuto - ponteiro_hora
    calc = x * 360
    angulo_atual = calc / 60
    if angulo_atual == angulo:
        print("Y")
        achou = True
        break
    if ponteiro_minuto == 59:
        ponteiro_minuto = 0

if achou is False:
    print("N")
