import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N,M = map(int,(input().split(' ')))

list_2 = []
for i in range(N):
    list_2.append(list(map(int,input().split(' '))))
for i in range(N):
    plus = list(map(int,input().split(' ')))

    for j in range(M):
        list_2[i][j] += plus[j]
for i in list_2:
    print(*i)