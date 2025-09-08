import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

dic = [0] * 9
for i in list(map(int, sys.stdin.readline().rstrip())):
    if i == 9:
        dic[6] += 1
    else:
        dic[i] += 1
dic[6] = (dic[6] + 1) // 2
print(max(dic))