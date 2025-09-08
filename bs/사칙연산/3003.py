import sys
sys.stdin = open('/Python/h.txt', 'r')

arr = [1, 1, 2, 2, 2, 8]

x = list(map(int,input().split()))
for i in range(6):
    print(arr[i] - x[i] , end=" ")
