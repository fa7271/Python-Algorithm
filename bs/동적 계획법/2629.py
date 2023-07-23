import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')


N = int(input()); lst = list(map(int,sys.stdin.readline().rstrip().split(" ")))
marble = int(input()); check_marble = list(map(int,sys.stdin.readline().rstrip().split(" ")))

# 추를 더해주거나 빼주거나
dp =[0]
for i in lst:
    res = []
    for j in dp:
        res.append(j+i)
        res.append(abs(j-i)) # 음수 방지
    dp = list(set(dp+res))
for i in check_marble:
    if i in dp:
        print("Y",end=" ")
    else:
        print("N",end=" ")


