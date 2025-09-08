import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

for _ in range(3):
    n = int(input())
    coins = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

    # 홀수 금액 애초에 못 나눔

    t = sum(i[0] * i[1] for i in coins)
    if t % 2 != 0:
        print(0)
        continue
    # 절반만 채우면 됨
    e = t // 2
    # 0 원은 가능
    dp = [True] + [False] * e
    flag =False
    # 절반으 맞추면 나머지는 다른애가 걍 다먹으면 된다.
    for coin, count in coins:
        for k in range(e, coin - 1, -1):
            if dp[k - coin]:
                for i in range(count):
                    if k + coin * i <= e:
                        dp[k + coin * i] = True
                    else:
                        break
        if dp[-1]:
            flag = True
            break
    print(1 if flag else 0)
