import sys
sys.stdin = open('/Python/h.txt', 'r')

# input = sys.stdin.readline
import sys
n = int(sys.stdin.readline())
b = [0] * 10001                 # 숫자 범위 설정
for i in range(n):              # 숫자 갯수만큼 포문
    b[int(sys.stdin.readline())] += 1   # 그 숫자 +1
for i in range(10001):              # 0
    if b[i] != 0:                   # 배열에 있으면
        for j in range(b[i]):       # b[5]
            print(i)                # 배열안에 있는 갯수 만큼 출력 ex)b[2] 는 2개 >> 2개 출력

        # for 문 없이 print(i) 만 쓰면 중복된거 제거돼서 1이 2개 이여도 1개만 출력됨

