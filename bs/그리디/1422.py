import sys
from collections import defaultdict

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

# lst = [["jpa 010-1111-2222"],
#        ["abc 010–7777-2222"],
#        ["bbc 010–7778-2222"],
#        ["abc 010–0778-3222"],
#        ["so 010–1778-3222"],
#        ["so 010–0778-3222"],
#        ["aaaa 010–0778-3222"],
#        ["aaaa 010–0778-3221"],
#        ["aaaa 010–0778-0221"],
#        ["jpa 010–0111-2222"],
#        ["jpa 010–0111-1222"]]
#
# res = []
# for i in lst:
#     res.append((i[0].split(" ")))
# res.sort(key=lambda x: (x[0], x[1][0:3], x[1][4:8], x[1][9:13]))
# print(res)

n, m = map(int, sys.stdin.readline().split(" "))
lst = [str(input()) for _ in range(n)]
lst.sort(key=lambda x: x * 9, reverse=True)
# 딱 맞게 줌
if len(lst) == m:
    print("".join(lst))
    exit()
# 안 맞아서 숫자 더 뽑아야함, 가장길고 큰걸로 뽑음
lst.sort(key=len, reverse=True)  # sort = nlogn // max,min = n
for i in range(m - len(lst)):
    lst.append(lst[0])
lst.sort(key=lambda x: x * 9, reverse=True)
print("".join(lst))
