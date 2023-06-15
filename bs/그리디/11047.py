import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N,M= map(int, input().split())

lst = [int(sys.stdin.readline().rstrip()) for i in range(N)]
count = 0
print(lst)
if M < lst[0]:
    print(0)

else:
    num = N-1
    while num >= 0:
        if M >= lst[num]:
            count += M // lst[num]
            M %= lst[num]
        num -= 1
print(count)


#
N, M = map(int, input().split())

coins = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
coins.sort()  # 동전의 가치를 오름차순으로 정렬

count = 0

for coin in coins:
    while M >= coin:
        count += 1
        M -= coin

print(count)