from math import ceil

alph = list(input('Введите словарь'))
countt = input("Введите частоты для словаря через пробел").split(' ')

if len(alph) != len(countt):
    print('неправильный ввод')
else:
    countt = [int(x) for x in countt]
    mass_ans = [[] * 10]
    mass_help = [[] * 10]
    countt_change = [countt[d:d+ceil(len(alph)/10)] for d in range(0, len(countt), ceil(len(alph)/10))]
    for _ in range(2):
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