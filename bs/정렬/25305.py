import sys
from collections import Counter # 최빈값 구하는 클래스
sys.stdin = open('/Python/h.txt', 'r')

# input = sys.stdin.readline
# input = int(sys.stdin.readline())


N,K = map(int,input().split(" ")) # N: 학생 수 K: 수상자
print(sorted(map(int,input().split(" ")), reverse = True)[K-1])

