import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')


n = int(input())
for _ in range(n):
    t= int(input())
    arr = sorted(list(map(int,sys.stdin.readline().rstrip().split(" "))))
    print(arr[0],arr[-1])