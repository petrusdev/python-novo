print('-' * 29)
print('|      TABELA DE  JOGOS     |')
print('-' * 29)

times = []
time1 = input('Digite time: ')
time2 = input('Digite time: ')
time3 = input('Digite time: ')

times.append(time1)
times.append(time2)
times.append(time3)

for time1 in times:
    for time2 in times:
        if time1 != time2:
            print(f'{time1} x {time2}')

