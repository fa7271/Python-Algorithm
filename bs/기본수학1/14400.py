import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')


N = int(input())
lst = [list(map(int,sys.stdin.readline().rstrip().split(" "))) for _ in range(N)]
x = sorted(lst, key=lambda x:x[0])[N//2][0] # x 중앙값
y = sorted(lst, key=lambda x:x[1])[N//2][1] # y 중앙값

res = sum([abs(x1-x) + abs(y1-y) for x1,y1 in lst])
print(res)

