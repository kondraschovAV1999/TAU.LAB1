n = int(input())
for j in range(0, 4):
    for i in range(1, n + 1):
        t = ('+___ ', '|' + str(i) + ' / ', '|__\\ ', '|    ')
        print(t[j], end='')
    print()

# print('+___  ')
# print('|', i, ' /', sep='')
# print('|__\\',
#       '|', sep='\n')
# print(t[0], t[1] + str(t[2]) + t[3], t[4], t[5], sep='\n', end=' ')
