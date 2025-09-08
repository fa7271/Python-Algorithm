from itertools import combinations
import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N, K = map(int,input().split(" "))


word = {"a","t","i","c","n"}
candidate = set(chr(i) for i in range(97, 123)) - word
words = [sys.stdin.readline().rstrip() for _ in range(N)]
remain_sets = [set(w) - word for w in words]
if K < 5:
    print(0)
else:
    res = 0
    for i in combinations(candidate,K-5):
        lst = set(i)
        count = 0
        for s in remain_sets:
             if lst.issuperset(s): # lst가 s를 가지고있냐
                count += 1
        res = max(count,res)

    print(res)


