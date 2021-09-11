n = int(input())
question = set(input().split())
answer = ''
help1 = set(map(str, range(1, n + 1)))
while 'HELP' not in question:
    if 'HELP' in question:
        break
    answer = input()
    if answer == 'YES':
        help1 &= question
    else:
        help1 -= (help1 & question)
    question = set(input().split())
print(*sorted(list(map(int, help1))))
