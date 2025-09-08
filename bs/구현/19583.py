import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

#시작, 끝, 스트리밍 끝
S, E, Q = input().split(" ")
dic = dict()
res =set()
for i in sys.stdin:
    time, name = i.rstrip().split(" ")
    # 개강총회 시작전에 들어온 사람
    if time <= S:
        dic[name] = time
    elif E <= time <= Q:
        if name in dic:
            res.add(name)
print(len(res))
