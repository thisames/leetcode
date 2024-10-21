# https://judge.beecrowd.com/pt/problems/view/1241

N = int(input())
words = [input() for _ in range(N)]

for word in words:
    nao_encaixa = False
    word = word.split(" ")
    if len(word[1]) > len(word[0]):
        print("nao encaixa")
        continue
    for i in range(len(word[1])):
        if word[1][-1 - i] != word[0][-1 - i]:
            print("nao encaixa")
            nao_encaixa = True
            break
    if not nao_encaixa:
        print("encaixa")
