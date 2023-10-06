import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')
n, k = map(int, input().split())

check = k*(k+1) //2 # 등차수열 합
if n < check: # 최소 합은 1 ~ 순서대로합 이여야함
    print(-1)
elif (n - check) % k == 0:
    # 나누어 떨이진다. 등차수열 만큼 들어가 있음 예를들면 2,3,4 개수 >> k-1
    print(k-1)
else:
    print(k)
# N개의 공을
# K개의 바구니에 빠짐없이 나누어 담는다.
# 각 바구니에는 1개 이상의 공이 들어 있어야 한다.
# 각 바구니에 담긴 공의 개수는 모두 달라야 한다.
# 가장 많이 담긴 바구니와 가장 적게 담긴 바구니의 공의 개수 차이가 최소가 되어야 한다.