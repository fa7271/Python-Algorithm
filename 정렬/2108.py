import sys
from collections import Counter # 최빈값 구하는 클래스
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt','r')

# input = sys.stdin.readline
# input = int(sys.stdin.readline())

N = int(sys.stdin.readline())
array = list()
for _ in range(N):
    array.append(int(sys.stdin.readline()))
sort = sorted(array)

print(round(sum(sort)/N))                      # 산술평균
print(sort[N//2])                        # 중앙값

count = Counter(sort).most_common(2)       # 빈도수가 높은 2개 함수 가져옴
if len(count) > 1 and count[0][1] == count[1][1]:
    print(count[1][0])
else:
    print(count[0][0])

print(max(array)-min(array))             # 최대범위

