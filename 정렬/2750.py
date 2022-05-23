import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt','r')

input = sys.stdin.readline

array = list()                        # 숫자 담을 리스트
N = int(input())
for i in range(N):
    a = int(input())
    array.append(a)                     # 숫자들 리스트에 담음

new = sorted(array)                     # 오름차순 정리한거 새로 만듦
for i in new:                           # 포문돌려서
    print(i)                            # 순서대로 출력



