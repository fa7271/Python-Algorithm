import sys
sys.stdin = open('/Python/h.txt', 'r')

import sys
input = sys.stdin.readline

s= set()
for i in range(10):
    s.add((int(input())%42))
print(len(s))


