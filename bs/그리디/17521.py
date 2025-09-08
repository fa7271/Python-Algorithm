import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n, w = map(int, sys.stdin.readline().split(" "))  # 날짜 n, 자본 w
lst = [int(sys.stdin.readline()) for _ in range(n)]

count = 0
for i in range(n-1):
    print(count,i, w)
    if lst[i] < lst[i+1]:  # 현재 주식 가격이 다음 날 주식 가격보다 작은 경우
        if w // lst[i] > 0:  # 자본으로 해당 주식을 구매할 수 있는 경우
            count = w // lst[i]  # 구매 가능한 주식 수를 계산하여 count에 저장
            w = w % lst[i]  # 남은 자본을 계산
    elif lst[i] > lst[i+1]:  # 현재 주식 가격이 다음 날 주식 가격보다 큰 경우
        w += count * lst[i]  # 보유한 주식을 판매하여 자본을 늘림
        count = 0  # 보유한 주식 수를 0으로 초기화
if count != 0:
    w += count * lst[-1]  # 보유한 주식이 남아 있는 경우, 가장 마지막 날의 주식 가격에 대한 계산
