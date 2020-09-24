from math import ceil
import numpy as np

alph = list(input("Введите словарь"))
countt = input('Введите частоты через пробел')


if len(alph) == len(countt) or len(alph) < 10:
    print('неправильный ввод')
else:
    countt = np.array(countt.split(' '))
    countt = [int(x) for x in countt]
    countt_change = np.array_split(countt, 10)

    for i in range(len(countt_change)):
        countt_change[i] = list(countt_change[i])

    for _ in range(ceil(len(countt) ** 0.5)):
        for j in range(len(countt_change) - 1):
            sum1 = 0
            sum2 = 0
            sum3 = 0
            if len(countt_change[j]) != 1 and len(countt_change[j + 1]) != 1:
                for i in range(len(countt_change[j])):
                    sum1 += (i + 1) * countt_change[j][i]
                for i in range(len(countt_change[j + 1])):
                    sum2 += (i + 2) * countt_change[j + 1][i]
                    if i >= 1:
                        sum3 += i * countt_change[j + 1][i]
                if sum1 - (countt_change[j][-1] * len(countt_change[j])) > sum2 + countt_change[j][-1]:
                        num = countt_change[j][-1]
                        countt_change[j].pop(-1)
                        countt_change[j + 1].insert(0, num)
                elif sum1 + (countt_change[j + 1][0] * len(countt_change[j])) < sum3:
                    num = countt_change[j + 1][0]
                    countt_change[j + 1].pop(0)
                    countt_change[j].append(num)


    for i in range(len(countt_change)):
        for j in range(len(countt_change[i])):
            countt_change[i][j] = alph[i + j]
    print(countt_change)
    #print(flag)
