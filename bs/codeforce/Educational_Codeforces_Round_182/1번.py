import sys
from itertools import combinations

sys.stdin = open('/Users/song/Desktop/Python/h.txt', 'r')

T = int(input())
for i in range(T):

    n = int(input())
    flag =False
    lst = [i for i in range(1, n + 1)]
    arr = list(map(int, sys.stdin.readline().split(" ")))
    for i in list(combinations(lst, 2)):
        left, right = i
        l = sum(arr[:left]) % 3
        m = sum(arr[left:right]) % 3
        r = sum(arr[right:]) % 3

        if (l != m and r != m and r!=l) or l == m == r:
            print(left,right)
            flag = True
            break
    if not flag:
        print(0,0)

#  24 분
