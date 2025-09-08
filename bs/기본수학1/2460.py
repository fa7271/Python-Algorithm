import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

sum_list = []
now = 0
for i in range(10):
    minus, plus = list(map(int,input().split(" ")))
    now += plus-minus
    sum_list.append(now)
print(max(sum_list))