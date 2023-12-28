import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n = int(input())
res = [0] * n
people = list(map(int,sys.stdin.readline().split(" ")))
for i in range(n):
    count = 0
    for j in range(n):
        if count == people[i] and res[j] == 0:
            res[j] = i+1
            break;
        elif res[j] == 0:
            count +=1
print(*res)


