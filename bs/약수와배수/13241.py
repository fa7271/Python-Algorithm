import sys
from collections import deque
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')
sys.setrecursionlimit(100000)


A,B = map(int,sys.stdin.readline().split(" "))

def gcd(x, y):  #최대공약수 구하기
    if y == 0:
        return x
    else:
        return gcd(y, x%y)

def lcm(x, y):  ## 최소공배수 구하기
    result = (x*y) // gcd(x,y)
    return result

print(lcm(A,B))