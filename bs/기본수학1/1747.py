import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n = int(input())

sosu = [True] * (2000001)
sosu[1] = False
m = int(2000000)
for i in range(2,m+1):
    if sosu[i]:
        for j in range(i*2, m+1, i):
            sosu[j] = False
def pel(x):
    x = str(x)
    if x == x[::-1]:
        print(int(x))
        exit()

for j in range(n, 2000001):

    if sosu[j] == True:
        pel(j)
# 71 프로
