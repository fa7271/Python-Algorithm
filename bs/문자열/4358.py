import sys
from collections import defaultdict
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

dic = defaultdict(int)
count = 0
while True:
    word = sys.stdin.readline().rstrip()
    if word == "":
        break
    dic[word] += 1
    count += 1

for k,v in sorted(dic.items()):
    per = round(v / count * 100, 4)
    print(k,per)

