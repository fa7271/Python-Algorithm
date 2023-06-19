import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')


K = int(sys.stdin.readline())

def hanoi(n,i,j,via):
    if n == 1:
        print(i,j)
    else:
        hanoi(n-1,i,via,j)
        print(i,j)
        hanoi(n-1,via,j,i)
print(2**K -1)
if K<=20:
    hanoi(K,1,3,2)

