import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

city = int(sys.stdin.readline())
roads = list(map(int, sys.stdin.readline().rstrip().split(" ")))
price = list(map(int, sys.stdin.readline().rstrip().split(" ")))


res = roads[0] * price[0]
idx = price[0] # 처음에는 무조건 기름 넣어야함, 최솟값

for i in range(1,city-1): # 1부터 마지막꺼는 도착 후라 필요없음
    if idx > price[i]: # 뒤에 기름값이 더쌈
        idx = price[i] # 뒤에 기름으로 바꿔주고

    res += idx * roads[i] # 뒷 기름과 가야하는 거리 곱해서 res에 넣어줌

print(res)




