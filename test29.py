import itertools
print(*map(lambda x: ''.join(x), map(list, itertools.permutations(map(str, range(1, int(input()) + 1))))), sep='\n')
