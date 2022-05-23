import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt','r')

input = sys.stdin.readline

array = list()                        # 숫자 담을 리스트
N = int(input())
for i in range(N):
    array.append(int(sys.stdin.readline()))

new = sorted(array)

for i in new:
    print(i)




