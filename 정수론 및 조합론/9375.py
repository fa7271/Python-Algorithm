import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

input = sys.stdin.readline
# input = int(sys.stdin.readline())

from collections import Counter
t = int(input())
for i in range(t):
    n = int(input())
    s = []                      # 리스트 생성

    for j in range(n):
        a, b = input().split()
        s.append(b)
    num = 1
    result = Counter(s)
    # print(result)
    for k in result:
        num *= result[k] + 1


    print(num - 1)

# Counter 함수를 사용해 많이 쓰인것들을 받아옴

