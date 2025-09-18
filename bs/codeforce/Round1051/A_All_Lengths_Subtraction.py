import heapq
import sys
sys.stdin = open('/Users/song/Desktop/Python/h.txt', 'r')

t = int(input())

# 최소 총비
for _ in range(t):
    n, k = map(int, input().split())
    price = sorted(list(map(int, input().split())))
    value = sorted(list(map(int, input().split())), reverse=True)

    x = []
    for i in price:
        heapq.heappush(x,(-i,-1))

    res = 0
    while x:
        # 할인 쿠폰 개수 작은거부터
        try:
            count = value.pop()
            if count > len(x):
                break
            temp = []
            # 쿠폰 갯수 만큼 돌아서 temp에 바뀌는거 넣음
            for node in range(count):
                d = -heapq.heappop(x)[0]
                temp.append(d)
            # 1개씩은 공짜임
            if len(temp) >= 2:
                res += sum(temp[0:len(temp)-1])
        except:
            break
    while x:
        res += -heapq.heappop(x)[0]
    print(res)



