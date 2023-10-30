import sys
from collections import deque, defaultdict

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

# 총갯수, 초밥갯수, 연속먹는갯수, 쿠폰번호
n, d, k, c = map(int,input().split(" "))
lst = [int(input()) for _ in range(n)]
dic = defaultdict(int)
# 쿠폰을 사용해 먹는 경우이니
# 쿠폰 무조건 먹는다고 판단한다.
dic[c] = 1

# 처음 k개 연속 먹기
for i in range(k):
    dic[lst[i]] += 1

# 투 포인터
left = 0; right = k-1
# 초기 결과값
res = -1e9
for i in range(n):
    #딕셔너리에서 왼쪽꺼는 빼주고, 오른쪽꺼는 더해줘야함
    res = max(res,len(dic))
    dic[lst[left]] -= 1
    if dic[lst[left]] == 0:
        del dic[lst[left]]
    left += 1; right += 1
    dic[lst[right%n]] += 1
print(res)