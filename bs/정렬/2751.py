import sys
sys.stdin = open('/Python/h.txt', 'r')

input = sys.stdin.readline

array = list()                        # 숫자 담을 리스트
N = int(input())
for i in range(N):
    array.append(int(sys.stdin.readline()))

new = sorted(array)
sys.stdout.write('\n'.join(map(str,new)))
# for i in new:
#     print(i)


# 조인 함수사용시  164440 kb / 1236 ms
# for 문 사용시   83488 kb / 1480 ms
