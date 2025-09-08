import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')
from collections import deque


N,C = map(int, sys.stdin.readline().split(" "))

lst = []
for i in range(N):
    lst.append(int(sys.stdin.readline()))
lst.sort()

start = 1 #  첫집은 무조건 가야지 최댓값 나올수 있음
end = lst[-1] - lst[0] # 최댓거리
res = 0
while start <= end:
    now = lst[0]
    count = 1 # 첫집 무조건 설치
    mid = (start + end) // 2
    for i in range(1,N):
        if lst[i] - now >= mid :# 설치해야하는곳
            count +=1
            now = lst[i] # 다음 공유기 설치한 값으로 옮김 그래야지 그 다음 차이가 mid 보다 크면 설치하기 위해서
    if count >= C: # 주어진 갯수 이상 설치하면
        if res < mid:
            res = mid
        start = mid +1
    else:
        end = mid - 1 # 설치 갯수가 부족하므로, 거리를 줄여준다.
print(res)

# 짝수면 왼쪽 , 오른쪽 차이
# 홀수면 왼쪽, 오른쪾중과 가운뎃 값 차이중 큰걸로









