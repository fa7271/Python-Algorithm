import sys
from collections import Counter # 최빈값 구하는 클래스
sys.stdin = open('/Python/h.txt', 'r')

# input = sys.stdin.readline
# input = int(sys.stdin.readline())


N = int(sys.stdin.readline())
array = []

for i in str(N):
    array.append(i)

array.sort(reverse=True)

print(''.join(array))

# changesorted = sorted(array)
# print(changesorted)

sort / sorted
reverse / reversed

sort/revers 는 정렬해서 반환하지만
reversed 와 sorted 는 다른 변수에 저장해야한다.